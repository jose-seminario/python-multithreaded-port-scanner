import time

from scanner import scan_port_range
from ui import show_banner, show_menu, show_scan_results, show_scan_time
from input_handler import (
    get_user_option,
    get_ip,
    get_port_range,
)

show_banner()
show_menu()

option = get_user_option()

if option == 1:
    ip = get_ip()
    start_port, end_port = get_port_range()

    start_time = time.time()

    open_ports = scan_port_range(ip, start_port, end_port)

    end_time = time.time()

    elapsed_time = end_time - start_time

    show_scan_results(open_ports)
    show_scan_time(elapsed_time)

elif option == 2:
    ip = get_ip()

    start_time = time.time()

    open_ports = scan_port_range(ip, 1, 65535)

    end_time = time.time()

    elapsed_time = end_time - start_time

    show_scan_results(open_ports)
    show_scan_time(elapsed_time)