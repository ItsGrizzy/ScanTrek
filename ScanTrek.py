import asyncio
import socket
import subprocess
import sys
import json
import signal
import os
import time
import random
from ipaddress import ip_address, ip_network
from tqdm import tqdm
from colorama import init, Fore, Back, Style
import shutil
from datetime import datetime

# Initialize colorama
init(autoreset=True)

# Global flag for clean exit
exit_flag = False

# Terminal dimensions
TERM_WIDTH = shutil.get_terminal_size().columns
TERM_HEIGHT = shutil.get_terminal_size().lines

# Signal handler for clean exit
def signal_handler(sig, frame):
    global exit_flag
    print(f"\n\n{Fore.RED}⚡ SCAN INTERRUPTED! Terminating all connections...")
    exit_flag = True
    time.sleep(1)
    print(f"{Fore.GREEN}✓ All connections terminated. System secure.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Configuration for reliable scanning
PORT_SCAN_TIMEOUT = 1.5
MAX_CONCURRENT_PER_HOST = 500
NMAP_CONCURRENCY = 3

# Print header
def print_header():
    """Print the header"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # ASCII Banner
    banner = [
        f"{Fore.CYAN}╔════════════════════════════════════════════════════════════════════════════════════════╗",
        f"{Fore.CYAN}║{Fore.BLUE} █████████                                ███████████                    █████     {Fore.CYAN}     ║",
        f"{Fore.CYAN}║{Fore.BLUE} ███░░░░░███                              ░█░░░███░░░█                   ░░███      {Fore.CYAN}    ║",
        f"{Fore.CYAN}║{Fore.BLUE}░███    ░░░   ██████   ██████   ████████  ░   ░███  ░  ████████   ██████  ░███ █████{Fore.CYAN}    ║",
        f"{Fore.CYAN}║{Fore.BLUE}░░█████████  ███░░███ ░░░░░███ ░░███░░███     ░███    ░░███░░███ ███░░███ ░███░░███ {Fore.CYAN}    ║",
        f"{Fore.CYAN}║{Fore.BLUE} ░░░░░░░░███░███ ░░░   ███████  ░███ ░███     ░███     ░███ ░░░ ░███████  ░██████░  {Fore.CYAN}    ║",
        f"{Fore.CYAN}║{Fore.BLUE} ███    ░███░███  ███ ███░░███  ░███ ░███     ░███     ░███     ░███░░░   ░███░░███ {Fore.CYAN}    ║",
        f"{Fore.CYAN}║{Fore.BLUE}░░█████████ ░░██████ ░░████████ ████ █████    █████    █████    ░░██████  ████ █████{Fore.CYAN}    ║",
        f"{Fore.CYAN}║{Fore.BLUE} ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░    ░░░░░    ░░░░░      ░░░░░░  ░░░░ ░░░░░ {Fore.CYAN}    ║",
        f"{Fore.CYAN}║                                                                                        ║",
        f"{Fore.CYAN}║{Fore.GREEN}               ⚡ SCANTREK -- THE FASTEST PATH TO OPEN PORTS ⚡ {Fore.CYAN}                        ║                           ",
        f"{Fore.CYAN}╚════════════════════════════════════════════════════════════════════════════════════════╝"
    ]
    
    for line in banner:
        print(line)
    
    print()
    print(f"{Fore.YELLOW}Author: {Fore.CYAN}Pratham Shah".center(TERM_WIDTH))
    print(f"{Fore.YELLOW}LinkedIn: {Fore.CYAN}https://www.linkedin.com/in/prathamshah529/".center(TERM_WIDTH))
    print()
    print(f"{Fore.MAGENTA}Initializing cyber scanning protocols...".center(TERM_WIDTH))
    print("\n" * 2)

# Print section header
def print_section_header(title):
    """Print section header with styling"""
    print(f"\n{Fore.CYAN}╔{'═' * (len(title) + 2)}╗")
    print(f"{Fore.CYAN}║ {Fore.YELLOW}{title.upper()} {Fore.CYAN}║")
    print(f"{Fore.CYAN}╚{'═' * (len(title) + 2)}╝{Style.RESET_ALL}")

# Port scanning functions
async def scan_port(host, port, sem, timeout=PORT_SCAN_TIMEOUT):
    try:
        async with sem:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(host, port),
                timeout=timeout
            )
            writer.close()
            await writer.wait_closed()
            return port
    except (asyncio.TimeoutError, ConnectionRefusedError):
        return None
    except Exception:
        return None

async def scan_host(host, ports):
    open_ports = []
    sem = asyncio.Semaphore(MAX_CONCURRENT_PER_HOST)
    tasks = [asyncio.create_task(scan_port(host, port, sem)) for port in ports]
    
    for future in asyncio.as_completed(tasks):
        if exit_flag:
            for task in tasks:
                task.cancel()
            break
        
        result = await future
        if result:
            open_ports.append(result)
    
    return (host, sorted(open_ports))

def run_fast_nmap(host, ports):
    output_file = f"nmap_{host}_{int(time.time())}.txt"
    port_str = ",".join(str(p) for p in ports)
    
    cmd = [
        "nmap",
        "-T4",
        "-A",
        "--min-hostgroup", "64",
        "--min-rate", "1000",
        "--max-retries", "1",
        "-Pn",
        "--version-intensity", "3",
        "-p", port_str,
        host,
        "-oN", output_file
    ]
    
    try:
        print(f"{Fore.BLUE}  [>] {Fore.CYAN}Starting deep scan for {Fore.GREEN}{host}")
        print(f"{Fore.BLUE}  [>] {Fore.CYAN}Results will be saved to: {Fore.YELLOW}{output_file}")
        
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        with open(output_file, "w") as f:
            f.write(result.stdout)
            
        return True, output_file
    except Exception as e:
        return False, str(e)

async def run_nmap_scans(results):
    completed = 0
    total = len(results)
    
    sem = asyncio.Semaphore(NMAP_CONCURRENCY)
    
    async def run_single_nmap(host, ports):
        async with sem:
            success, output = await asyncio.get_event_loop().run_in_executor(
                None, 
                lambda: run_fast_nmap(host, ports)
            )
            return host, success, output
    
    tasks = []
    for host, ports in results:
        tasks.append(asyncio.create_task(run_single_nmap(host, ports)))
    
    print(f"{Fore.BLUE}\n  [*] {Fore.CYAN}Initiating deep scan protocol...")
    print(f"{Fore.BLUE}  [*] {Fore.CYAN}Running {len(tasks)} scans concurrently")
    
    start_time = time.time()
    
    for future in asyncio.as_completed(tasks):
        host, success, output = await future
        completed += 1
        
        if success:
            print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Scan completed for {Fore.GREEN}{host}")
            print(f"{Fore.GREEN}       {Fore.CYAN}Results saved to: {Fore.YELLOW}{output}")
        else:
            print(f"{Fore.RED}  [✗] {Fore.CYAN}Scan failed for {Fore.GREEN}{host}: {Fore.RED}{output}")
        
        elapsed = time.time() - start_time
        print(f"{Fore.BLUE}  [*] {Fore.CYAN}Progress: {completed}/{total} ({elapsed:.1f}s)")
    
    return completed

def save_results(results, filename, fmt):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename}_{timestamp}"
    
    if fmt == "txt":
        output_file = f"{filename}.txt"
        with open(output_file, "w") as f:
            f.write("ScanTrek Port Scan Results\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")
            for host, ports in results:
                f.write(f"Host: {host}\n")
                f.write(f"Open Ports: {', '.join(map(str, ports))}\n")
                f.write("-" * 50 + "\n")
        print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Scan results saved to: {Fore.YELLOW}{output_file}")
    elif fmt == "csv":
        output_file = f"{filename}.csv"
        with open(output_file, "w") as f:
            f.write("Host,Port\n")
            for host, ports in results:
                for port in ports:
                    f.write(f"{host},{port}\n")
        print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Scan results saved to: {Fore.YELLOW}{output_file}")
    elif fmt == "json":
        output_file = f"{filename}.json"
        data = {
            "scan_date": datetime.now().isoformat(),
            "results": [{"host": host, "open_ports": ports} for host, ports in results]
        }
        with open(output_file, "w") as f:
            json.dump(data, f, indent=2)
        print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Scan results saved to: {Fore.YELLOW}{output_file}")

def parse_targets(target_input):
    targets = []
    host = target_input.strip()
    
    try:
        if "/" in host:
            net = ip_network(host, strict=False)
            return [str(ip) for ip in net.hosts()]
        if "-" in host:
            parts = host.split("-")
            if len(parts) == 2:
                start_ip = ip_address(parts[0])
                end_ip = ip_address(parts[1]) if "." in parts[1] else ip_address(
                    f"{'.'.join(parts[0].split('.')[:-1])}.{parts[1]}"
                )
                return [str(ip_address(ip)) 
                        for ip in range(int(start_ip), int(end_ip) + 1)]
        ip_address(host)
        return [host]
    except ValueError:
        try:
            return [socket.gethostbyname(host)]
        except socket.gaierror:
            print(f"{Fore.RED}  [!] {Fore.YELLOW}Could not resolve {host}. Using as-is.")
            return [host]
    return []

async def scan_all_hosts(hosts, ports):
    results = []
    total_tasks = len(hosts)
    
    with tqdm(total=total_tasks, desc=f"{Fore.BLUE}  [*] {Fore.CYAN}Scanning hosts", 
              bar_format="{l_bar}{bar:50}{r_bar}", ncols=TERM_WIDTH) as pbar:
        tasks = [asyncio.create_task(scan_host(host, ports)) for host in hosts]
        
        for future in asyncio.as_completed(tasks):
            try:
                host, open_ports = await future
                if open_ports:
                    results.append((host, open_ports))
                pbar.update(1)
                
                # Update status message
                pbar.set_description(f"{Fore.BLUE}  [*] {Fore.CYAN}Scanning {Fore.GREEN}{host}")
            except Exception:
                pbar.update(1)
    
    return results

def get_user_input(prompt, color=Fore.CYAN):
    """Get user input with colored prompt"""
    print(f"{Fore.BLUE}  [?] {color}{prompt}{Style.RESET_ALL}", end="")
    return input().strip()

async def main_async():
    global exit_flag
    
    # Print header
    print_header()
    
    print_section_header("Target Acquisition")
    target_input = get_user_input("Enter IP, CIDR range, domain, or URL: ")
    if not target_input:
        print(f"{Fore.RED}  [!] {Fore.YELLOW}No input provided. Operation aborted.")
        return
        
    hosts = parse_targets(target_input)
    if not hosts:
        print(f"{Fore.RED}  [!] {Fore.YELLOW}No valid targets detected. Operation aborted.")
        return

    print_section_header("Scan Configuration")
    print(f"{Fore.BLUE}  [1] {Fore.CYAN}Standard Scan (Ports 1-1024)")
    print(f"{Fore.BLUE}  [2] {Fore.CYAN}Strategic Scan (Critical Ports)")
    print(f"{Fore.BLUE}  [3] {Fore.CYAN}Full Spectrum Scan (All Ports)")
    print(f"{Fore.BLUE}  [4] {Fore.CYAN}Custom Target Scan")
    choice = get_user_input("Select scan type [1-4]: ")
    
    if choice == "2":
        ports = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
        print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Selected: Strategic Scan ({len(ports)} ports)")
    elif choice == "3":
        ports = list(range(1, 65536))
        print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Selected: Full Spectrum Scan (All 65,535 ports)")
    elif choice == "4":
        custom = get_user_input("Enter ports (e.g., 1-100 or 22,80,443): ")
        if "-" in custom:
            start, end = custom.split("-", 1)
            try:
                ports = list(range(int(start), int(end) + 1))
                print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Selected: Custom Range Scan ({len(ports)} ports)")
            except:
                ports = list(range(1, 1025))
                print(f"{Fore.RED}  [!] {Fore.YELLOW}Invalid range. Using Standard Scan")
        else:
            ports = [int(p.strip()) for p in custom.split(",") if p.strip().isdigit()]
            if not ports:
                ports = list(range(1, 1025))
                print(f"{Fore.RED}  [!] {Fore.YELLOW}No valid ports. Using Standard Scan")
            else:
                print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Selected: Custom Port Scan ({len(ports)} ports)")
    else:
        ports = list(range(1, 1025))
        print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Selected: Standard Scan (Ports 1-1024)")

    print_section_header("Output Configuration")
    print(f"{Fore.BLUE}  [1] {Fore.CYAN}Text Report (TXT)")
    print(f"{Fore.BLUE}  [2] {Fore.CYAN}Data Sheet (CSV)")
    print(f"{Fore.BLUE}  [3] {Fore.CYAN}Structured Data (JSON)")
    fmt_choice = get_user_input("Select output format [1-3]: ")
    
    if fmt_choice == "2":
        fmt = "csv"
        print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Selected: Data Sheet (CSV)")
    elif fmt_choice == "3":
        fmt = "json"
        print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Selected: Structured Data (JSON)")
    else:
        fmt = "txt"
        print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Selected: Text Report (TXT)")

    print_section_header("Scan Initiation")
    print(f"{Fore.BLUE}  [*] {Fore.CYAN}Targets: {Fore.GREEN}{len(hosts)}")
    print(f"{Fore.BLUE}  [*] {Fore.CYAN}Ports per target: {Fore.GREEN}{len(ports)}")
    print(f"{Fore.BLUE}  [*] {Fore.CYAN}Total operations: {Fore.GREEN}{len(hosts)*len(ports):,}")
    print(f"{Fore.BLUE}  [*] {Fore.CYAN}Initiating scan sequence...")
    
    try:
        start_time = time.time()
        results = await scan_all_hosts(hosts, ports)
        scan_time = time.time() - start_time
        
        print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Scan completed in {Fore.GREEN}{scan_time:.1f}s")
        
        save_results(results, "ScanTrek_Report", fmt)
        
        if results:
            print_section_header("Scan Results")
            print(f"{Fore.BLUE}  [*] {Fore.CYAN}Hosts with open ports: {Fore.GREEN}{len(results)}")
            for host, ports_found in results:
                print(f"{Fore.BLUE}  [+] {Fore.GREEN}{host}{Fore.CYAN}: {len(ports_found)} open ports")
                print(f"      {Fore.YELLOW}{', '.join(map(str, ports_found))}")
            
            print_section_header("Deep Scan Protocol")
            if input(f"{Fore.BLUE}  [?] {Fore.CYAN}Execute deep scan protocol? (y/N): ").strip().lower() == "y":
                print(f"{Fore.BLUE}  [*] {Fore.CYAN}Initializing deep scan sequence...")
                nmap_start = time.time()
                completed = await run_nmap_scans(results)
                nmap_time = time.time() - nmap_start
                print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Deep scan completed: {Fore.GREEN}{completed} hosts")
                print(f"{Fore.GREEN}       {Fore.CYAN}Elapsed time: {Fore.GREEN}{nmap_time:.1f}s")
            else:
                print(f"{Fore.YELLOW}  [*] {Fore.CYAN}Deep scan protocol aborted")
        else:
            print(f"{Fore.YELLOW}  [!] {Fore.CYAN}No open ports detected on any targets")
            
        print_section_header("Operation Complete")
        print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Total scan time: {Fore.GREEN}{scan_time:.1f}s")
        print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Targets scanned: {Fore.GREEN}{len(hosts)}")
        print(f"{Fore.GREEN}  [✓] {Fore.CYAN}Ports scanned per target: {Fore.GREEN}{len(ports)}")
        print(f"{Fore.BLUE}  [*] {Fore.CYAN}System returning to normal operation...")

    except KeyboardInterrupt:
        print(f"{Fore.RED}  [!] {Fore.YELLOW}Scan sequence interrupted by user")
        sys.exit(0)

def main():
    # Windows compatibility
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    # Run the main async function
    asyncio.run(main_async())
    
    # Final message
    print(f"\n{Fore.CYAN}╔{'═' * (TERM_WIDTH - 2)}╗")
    print(f"║ {Fore.GREEN}SCANTREK OPERATION COMPLETE. SYSTEM SECURE. {Fore.CYAN}║".center(TERM_WIDTH - 2))
    print(f"╚{'═' * (TERM_WIDTH - 2)}╝")

if __name__ == "__main__":
    # Check for dependencies
    try:
        import colorama
    except ImportError:
        print("Colorama module not found. Please install with: pip install colorama")
        sys.exit(1)
        
    try:
        main()
    except Exception as e:
        print(f"{Fore.RED}Critical error: {e}")
        sys.exit(1)
