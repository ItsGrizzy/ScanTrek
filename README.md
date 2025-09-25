# ScanTrek: Ultimate Port Scanner ⚡
* In Process by 25-09-2025 *
The Fastest Port Scanner for Security Professionals
Find open ports faster than ever before! ScanTrek is the next-generation port scanner that combines blazing speed with military-grade precision to map your network in record time. Built for security professionals, network admins, and ethical hackers who demand both speed and accuracy.

![ScanTrek Banner](https://github.com/ItsGrizzy/ScanTrek/blob/main/ScanTrek.png)

## ❓ Why I Built ScanTrek

I created ScanTrek to solve a critical problem: traditional port scanners are either too slow for large networks or lack the depth needed for serious security work. My mission was to build a tool that delivers:

- ⚡ **Lightning-fast results** — 25 seconds for 131,000+ port checks  
- 🎯 **Pinpoint accuracy** — Intelligent host discovery  
- 🏢 **Enterprise-grade features** — Intuitive interface  
- 🔎 **Deep scanning capabilities** — Beyond surface-level results  


## 🔥 Key Features That Set ScanTrek Apart

- **Military-Grade Speed**  
  Scan entire subnets in seconds, not hours — 131,070 ports scanned in just **25 seconds**!

- **Smart Host Discovery**  
  Automatically detects active hosts before scanning, saving hours on dead IPs.

- **Four Powerful Scan Modes**  
  - 🟢 **Standard Scan** (Ports 1–1024)  
  - 🟠 **Strategic Scan** (200 critical ports)  
  - 🔵 **Full Spectrum Scan** (All 65,535 ports)  
  - 🛠️ **Custom Scan** (Select your own ports)

- **Deep Scan Integration**  
  One-click Nmap integration for detailed service analysis.

- **Professional Reporting**  
  Export results in **TXT**, **CSV**, or **JSON** formats.

- **Universal Target Support**  
  - **Single IP**: `192.168.1.1`  
  - **IP Range**: `192.168.1.1-100`  
  - **CIDR Block**: `10.0.0.0/24`  
  - **Domain**: `example.com`  
  - **URL**: `https://example.com`  
  - **File Input**: `targets.txt`

## 🚀 Mind-Blowing Performance
* Check what ScanTrek can do in under 30 seconds:
```
  [*] Targets: 2
  [*] Ports per target: 65535
  [*] Total operations: 131,070
  [*] Initiating scan sequence...
  [✓] Scan completed in 25.7s
```

## ⚙️ Installation & Setup
* Requirements
```
Python 3.7+
Nmap (for deep scanning - still optional)
```
### Quick Install
```
# Clone repository
git clone https://github.com/ItsGrizzy/ScanTrek.git
cd ScanTrek

# Install dependencies
pip install colorama tqdm

# Make script executable
chmod +x ScanTrek.py

# Create global symlink (run anywhere!)
sudo ln -s $(pwd)/ScanTrek.py /usr/local/bin/scantrek
```
### Run From Anywhere
```
# After creating symlink
scantrek
```
### Usage Demo
```
╔════════════════════════════════════════════════════════════════════════════════════════╗
║ █████████                                ███████████                    █████          ║
║ ███░░░░░███                              ░█░░░███░░░█                   ░░███          ║
║░███    ░░░   ██████   ██████   ████████  ░   ░███  ░  ████████   ██████  ░███ █████    ║
║░░█████████  ███░░███ ░░░░░███ ░░███░░███     ░███    ░░███░░███ ███░░███ ░███░░███     ║
║ ░░░░░░░░███░███ ░░░   ███████  ░███ ░███     ░███     ░███ ░░░ ░███████  ░██████░      ║
║ ███    ░███░███  ███ ███░░███  ░███ ░███     ░███     ░███     ░███░░░   ░███░░███     ║
║░░█████████ ░░██████ ░░████████ ████ █████    █████    █████    ░░██████  ████ █████    ║
║ ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░    ░░░░░    ░░░░░      ░░░░░░  ░░░░ ░░░░░     ║
║                                                                                        ║
║               ⚡ SCANTREK -- THE FASTEST PATH TO OPEN PORTS ⚡                         ║                           
╚════════════════════════════════════════════════════════════════════════════════════════╝

                                                Author: Pratham Shah                                               
                               LinkedIn: https://www.linkedin.com/in/prathamshah529/                               

                                        Initializing cyber scanning protocols...                                        

╔════════════════════╗
║ TARGET ACQUISITION ║
╚════════════════════╝
  [?] Enter IP, CIDR range, domain, URL, or file path: 10.200.107.1/24

╔════════════════╗
║ HOST DISCOVERY ║
╚════════════════╝
  [*] Multiple hosts detected (254). Performing host discovery...
  [*] Discovering active hosts: 100%|██████████████████████████████████████████████████| 254/254 [00:04<00:00, 61.94it/s]
  [✓] Found 2 active hosts

╔════════════════════╗
║ SCAN CONFIGURATION ║
╚════════════════════╝
  [1] Standard Scan (Ports 1-1024)
  [2] Strategic Scan (Critical Ports)
  [3] Full Spectrum Scan (All Ports)
  [4] Custom Target Scan
  [?] Select scan type [1-4]: 3
  [✓] Selected: Full Spectrum Scan (All 65,535 ports)

╔══════════════════════╗
║ OUTPUT CONFIGURATION ║
╚══════════════════════╝
  [1] Text Report (TXT)
  [2] Data Sheet (CSV)
  [3] Structured Data (JSON)
  [?] Select output format [1-3]: 1
  [✓] Selected: Text Report (TXT)

╔═════════════════╗
║ SCAN INITIATION ║
╚═════════════════╝
  [*] Targets: 2
  [*] Ports per target: 65535
  [*] Total operations: 131,070
  [*] Initiating scan sequence...
  [*] Scanning 10.200.107.33: 100%|██████████████████████████████████████████████████| 2/2 [00:25<00:00, 12.83s/it] 
  [✓] Scan completed in 25.7s
  [✓] Scan results saved to: ScanTrek_Report_20250807_035232.txt

╔══════════════╗
║ SCAN RESULTS ║
╚══════════════╝
  [*] Hosts with open ports: 2
  [+] 10.200.107.250: 2 open ports
      22, 1337
  [+] 10.200.107.33: 3 open ports
      22, 80, 33060

╔════════════════════╗
║ DEEP SCAN PROTOCOL ║
╚════════════════════╝
  [?] Execute deep scan protocol? (y/N): y
  [*] Initializing deep scan sequence...                                                                                     

  [*] Initiating deep scan protocol...                                                                                       
  [*] Running 2 scans concurrently
  [>] Starting deep scan for 10.200.107.250
  [>] Results will be saved to: nmap_10.200.107.250_1754553156.txt
  [>] Starting deep scan for 10.200.107.33
  [>] Results will be saved to: nmap_10.200.107.33_1754553156.txt
  [✓] Scan completed for 10.200.107.250
  [*] Progress: 1/2 (18.2s)
  [✓] Scan completed for 10.200.107.33
  [*] Progress: 2/2 (19.8s)
  [✓] Deep scan completed: 2 hosts
       Elapsed time: 19.8s

╔════════════════════╗
║ OPERATION COMPLETE ║
╚════════════════════╝
  [✓] Total scan time: 25.7s
  [✓] Targets scanned: 2
  [✓] Ports scanned per target: 65535
  [*] System returning to normal operation...

╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                                 ║ SCANTREK OPERATION COMPLETE. SYSTEM SECURE. ║                                 
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
```
## FAQ
Q: How fast is ScanTrek compared to other scanners? <br>
A: ScanTrek is 10-50x faster than traditional scanners, scanning 131,000+ ports in 25 seconds!

Q: Can I scan through firewalls? <br>
A: Yes! ScanTrek uses advanced techniques to detect hosts behind firewalls.

Q: What makes the deep scan special? <br>
A: Our one-click Nmap integration provides detailed service info without leaving the tool.

## License
ScanTrek is released under the [MIT License](https://github.com/ItsGrizzy/ScanTrek?tab=MIT-1-ov-file#readme)

## Disclaimer: 
Use ScanTrek only on networks you have explicit permission to scan. The developer assumes no liability for misuse. Always obtain proper authorization before scanning.


