def show_banner():
    print("*" * 42)
    print("         Python Port Scanner")
    print("*" * 42)


def show_menu():
    print("1. Scan a specific port or a port range")
    print("2. Scan all ports")

def show_scan_results(open_ports):
    for port, service in open_ports:
        print(f"Port: {port} | Service: {service}")

def show_scan_time(elapsed_time):
    print(f"Scan completed in {elapsed_time:.2f} seconds")

def show_progress(progress):
    print(f"Scanning... {progress:.2f}%", end="\r")