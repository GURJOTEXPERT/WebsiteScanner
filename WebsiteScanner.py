from utils.port_scan import scan_ports
from utils.ssl_scan import check_ssl
from utils.http_headers import fetch_http_headers
from utils.vulnerability_scan import check_xss, check_sqli
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 website_scanner.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    print(f"Starting scan for {url}")

    # Run the various scans
    scan_ports(url)
    check_ssl(url)
    fetch_http_headers(url)
    check_xss(url)
    check_sqli(url)

    print("[+] Scanning completed.")

if __name__ == "__main__":
    main()
