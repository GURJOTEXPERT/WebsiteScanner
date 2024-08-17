import subprocess

def check_ssl(url):
    try:
        print("Checking SSL/TLS security...")
        subprocess.run(['sslscan', url])
    except Exception as e:
        print(f"SSL scan failed: {e}")
