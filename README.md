# ScanTrek: Ultimate Port Scanner
The Fastest Port Scanner for Security Professionals
ScanTrek is a high-performance asynchronous port scanner designed for rapid network reconnaissance. Built with Python's asyncio library, it delivers lightning-fast scanning capabilities while maintaining accuracy. Whether you're scanning a single host or an entire network range, ScanTrek provides comprehensive port visibility with minimal resource consumption.

Why I Built ScanTrek: Traditional port scanners can be slow and resource-intensive when scanning large networks. I created ScanTrek to solve this problem - combining asynchronous I/O operations with intelligent scanning techniques to deliver results 10x faster than conventional scanners while maintaining enterprise-grade reliability.

## Key Features
⚡Blazing Fast Scans: Asynchronous architecture processes thousands of ports simultaneousl <br/>
⚡Multiple Target Formats: Supports single IPs, CIDR ranges, domains, and custom IP ranges <br/>
⚡Smart Port Selection: Predefined scan profiles and custom port ranges <br/>
⚡Nmap Integration: Detailed service scanning after port discovery <br/>
⚡Professional Reporting: TXT, CSV, and JSON output formats <br/>
⚡Real-time Progress Tracking: Visual progress bars and status updates <br/>

## Requirements

- **Python 3.7+**  
- **[nmap](https://nmap.org/)** (for deep scans)  
- **Python packages**:
  - `colorama`
  - `tqdm`

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/scantrek.git
   cd scantrek

2. **Create & activate a virtual environment (optional but recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Linux/macOS
   venv\Scripts\activate       # Windows PowerShell

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. ** Ensure nmap is in your PATH for deep scans **
    ````bash
    nmap --version

## Usage
**Run the main script:**
    
    python3 ScanTreak.py
** You will be prompted to **
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
# Enter IP, CIDR range, domain, or URL: (e.g. 192.168.1.0/24), range (192.168.1.10-20), or hostname.
  [?] Enter IP, CIDR range, domain, or URL: 192.168.1.71

╔════════════════════╗
║ SCAN CONFIGURATION ║
╚════════════════════╝
# Select Scan Type:
  [1] Standard Scan (Ports 1-1024)
  [2] Strategic Scan (Critical Ports)
  [3] Full Spectrum Scan (All Ports)
  [4] Custom Target Scan
  [?] Select scan type [1-4]: 3
  [✓] Selected: Full Spectrum Scan (All 65,535 ports)

╔══════════════════════╗
║ OUTPUT CONFIGURATION ║
╚══════════════════════╝
# Select Output Format:
  [1] Text Report (TXT)
  [2] Data Sheet (CSV)
  [3] Structured Data (JSON)
  [?] Select output format [1-3]: 1
  [✓] Selected: Text Report (TXT)

╔═════════════════╗
║ SCAN INITIATION ║
╚═════════════════╝
  [*] Targets: 1
  [*] Ports per target: 65535
  [*] Total operations: 65,535
  [*] Initiating scan sequence...
  [*] Scanning 192.168.1.71: 100%|██████████████████████████████████████████████████| 1/1 [00:03<00:00,  3.09s/it]
  [✓] Scan completed in 3.1s
  [✓] Scan results saved to: ScanTrek_Report_20250630_173118.txt

╔══════════════╗
║ SCAN RESULTS ║
╚══════════════╝
  [*] Hosts with open ports: 1
  [+] 192.168.1.71: 8 open ports
      21, 22, 1883, 3389, 5355, 8501, 8834, 14148

╔════════════════════╗
║ DEEP SCAN PROTOCOL ║
╚════════════════════╝
# After the fast asynchronous pass, you’ll see hosts with open ports. You can then choose to trigger the Deep Scan Protocol (Nmap) on discovered hosts. ( Yes/No )
  [?] Execute deep scan protocol? (y/N): y
  [*] Initializing deep scan sequence...                                                                                      

  [*] Initiating deep scan protocol...                                                                                        
  [*] Running 1 scans concurrently
  [>] Starting deep scan for 192.168.1.71
  [>] Results will be saved to: nmap_192.168.1.71_1751284884.txt
  [✓] Scan completed for 192.168.1.71
       Results saved to: nmap_192.168.1.71_1751284884.txt
  [*] Progress: 1/1 (55.9s)
  [✓] Deep scan completed: 1 hosts
       Elapsed time: 55.9s

╔════════════════════╗
║ OPERATION COMPLETE ║
╚════════════════════╝
  [✓] Total scan time: 3.1s
  [✓] Targets scanned: 1
  [✓] Ports scanned per target: 65535
  [*] System returning to normal operation...

╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
                                 ║ SCANTREK OPERATION COMPLETE. ║                                  
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝


```

[2] Data Sheet (CSV)

[3] Structured Data (JSON)

After the fast asynchronous pass, you’ll see hosts with open ports. You can then choose to trigger the Deep Scan Protocol (Nmap) on discovered hosts.
