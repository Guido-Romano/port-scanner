#!/usr/bin/env python3

import socket
from termcolor import colored
import threading
import ipaddress
import nmap
import time
import sys


# Function to validate an IP address
def validate_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False


# Function to scan a single port on the target host
def scan_port(host, port, open_ports, nm):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                if port not in open_ports:
                    open_ports.add(port)
                    sys.stdout.flush()
                    print(colored(f"[+] Port {port} open", "yellow"))

                    # Running an Nmap scan on the open port
                    nm.scan(host, str(port),
                            "-sS -T5 -A")
                    if port in nm[host]['tcp']:
                        service = nm[host]['tcp'][port]['name']
                        version = nm[host]['tcp'][port]['version']
                        product = nm[host]['tcp'][port]['product']
                        extra_info = nm[host]['tcp'][port].get('extrainfo', '')

                        print(colored(f"\n    Port: {port}", "yellow"))
                        print(colored(f"\033[3m    Service: {service}\033[0m",
                                      "white"))
                        print(colored(f"\033[3m    Version: {version}\033[0m",
                                      "white"))
                        print(colored(f"\033[3m    Product: {product}\033[0m",
                                      "white"))

                    if extra_info:
                        print(colored(f"Extra Info: {extra_info}",
                                      "white"))

                # Sending an HTTP request if the port is a common web port
                if port in [80, 443, 8080, 5426]:
                    message = (
                        f"GET / HTTP/1.1\r\n"
                        f"Host: {host} \r\n"
                        "User-Agent: port-scanner\r\n"
                        "Connection: close\r\n\r\n"
                    )
                    sock.sendall(message.encode())

                    chunks = []
                    while True:
                        chunk = sock.recv(8192)
                        if not chunk:
                            break
                        chunks.append(chunk)
                    data = b"".join(chunks)
                    print(colored
                          (f"Received from port {port}: {data}", "grey"))

    except socket.timeout:
        sys.stdout.write("\n")
        print(colored(f"Socket timeout on port {port}", "yellow"))
    except socket.error as err:
        print(colored(f"Socket error on port {port}: {err}", "yellow"))
    except Exception as e:
        print(colored(f"Error scanning port {port} on {host}: {e}", "red"))


# Main function to handle user input and start scanning
def main():
    host = input(colored("[*] Enter the IP address to scan: ", "magenta"))
    if not validate_ip(host):
        print(colored("[!] Invalid IP address", "red"))
        return

    nm = nmap.PortScanner()
    open_ports = set()

    # List of 100 common ports to scan
    common_ports = [
        21, 22, 23, 25, 53, 80, 101, 110, 111, 123,
        135, 136, 137, 138, 139, 143, 161, 179, 194, 389,
        443, 444, 445, 465, 513, 514, 548, 546, 547, 587,
        591, 631, 636, 853, 873, 902, 993, 990, 995, 1194,
        1433, 1521, 1701, 1723, 1812, 1813, 2049, 2082, 2083, 2086,
        2087, 2095, 2096, 3306, 3389, 4662, 4672, 5000, 5060, 5061,
        5222, 5400, 5432, 5500, 5800, 5900, 5938, 6881, 6969, 8080,
        8081, 8443, 10000, 32768, 49152, 49153, 49154, 49155, 49156, 49157,
        49158, 49159, 49160, 49161, 49163, 49165, 49167, 49175, 49176, 49400,
        51400, 6660, 6661, 6662, 6664, 6665, 6666, 6667, 6668, 6669
    ]

    # Creating threads for scanning multiple ports concurrently
    threads = [
        threading.Thread(target=scan_port, args=(host, port, open_ports, nm))
        for port in common_ports
    ]

    for thread in threads:
        thread.start()

    # Display scanning progress
    while any(thread.is_alive() for thread in threads):
        for i in range(4):
            sys.stdout.write(colored(f"\r[*] Still scanning{'.' * i}", "blue"))
            sys.stdout.flush()
            time.sleep(1)

    for thread in threads:
        thread.join()

    print(colored("\r[*] Scan complete.", "blue"))


# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
