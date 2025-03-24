#!/usr/bin/env python3

import socket
import threading


def scan_port(target_host, port):

    # Scan a specific port on the target host.

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Faster scans with a timeout
            if s.connect_ex((target_host, port)) == 0:
                print(f"Port {port} is open")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")


def scan_ports(target_host, start_port, end_port):

    # Scan ports in a range using threads to improve speed.

    print(f"Scanning {target_host} from port {start_port} to {end_port}")
    threads = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target_host, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Ensure all threads finish


def main():

    # Prompt for IP and start the scan.

    target = input("Enter the IP address to scan: ")  # User enters target IP
    scan_ports(target, 1, 65535)  # Scan all ports


if __name__ == "__main__":
    main()
