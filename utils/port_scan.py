import subprocess

def scan_ports(url):
    try:
        print("Scanning for open ports...")
        subprocess.run(['nmap', '-F', url])
    except Exception as e:
        print(f"Port scan failed: {e}")
