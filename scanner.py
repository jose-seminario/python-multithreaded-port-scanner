import socket
from concurrent.futures import ThreadPoolExecutor


def scanner(ip, port):
    connection = socket.socket()
    connection.settimeout(1)

    try:
        connection.connect((ip, port))
        return True

    except:
        return False

    finally:
        connection.close()


def get_service(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown"

def scan_port_range(ip, start_port, end_port):
    open_ports = []
    
    with ThreadPoolExecutor() as executor:
        futures = []

        for port in range(start_port, end_port + 1):
            future = executor.submit(scanner, ip, port)
            futures.append((future, port))
        
        for future, port in futures:
            result = future.result()

            if result:
                service = get_service(port)
                open_ports.append((port, service))