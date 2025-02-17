#!/usr/bin/env python3

import socket
from termcolor import colored
import threading
import ipaddress
import nmap
import time
import sys

# Record the start time of the script execution
start_time = time.time()


# Validate if the provided IP address is correctly formatted
def validate_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False


# Function to scan a specific port on the host
def scan_port(host, port, open_ports, nm):
    try:
        # Create a socket to connect to the port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                if port not in open_ports:
                    open_ports.add(port)
                    print(colored(f"[+] Port {port} open", "green"))

                    # Use nmap to scan the port for additional information
                    nm.scan(
                        host, str(port),
                        "-sS -sV -T4 -A --version-all "
                        "--script=default,vuln,discovery"
                            )

                    # Get detailed info about the open TCP port using nmap
                    if port in nm[host]['tcp']:
                        data = nm[host]['tcp'][port]
                        service = data.get('name', 'Unknown')
                        version = data.get('version', 'Unknown')
                        product = data.get('product', 'Unknown')
                        extra_info = data.get('extrainfo', '')

                        # Color-coded output for the service enumeration
                        print(colored(f"Port {port}", "magenta") +
                              colored(" \033[3m Service: \033[0m", "yellow") +
                              colored(f"\033[3m {service}\033[0m", "white") +
                              colored(" \033[3m Version: \033[0m", "yellow") +
                              colored(f"\033[3m {version}\033[0m", "white") +
                              colored(" \033[3m Product: \033[0m", "yellow") +
                              colored(f"\033[3m {product}\033[0m", "white") +
                              colored(f" \033[3m {extra_info}\033[0m", "grey")
                              )

                # Create and send an HTTP request to common web ports
                if port in [80, 443, 8080, 5426]:
                    try:
                        message = (
                            "GET / HTTP/1.1\r\n"
                            f"Host: {host} \r\n"
                            "User-Agent: Mozilla/5.0 "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/90.0.4430.212 Safari/537.36\r\n"
                            "Accept: text/html\r\n"
                            "Connection: close\r\n\r\n"
                        )

                        sock.sendall(message.encode())

                        chunks = []
                        while True:
                            chunk = sock.recv(2048)
                            if not chunk:
                                break
                            chunks.append(chunk)
                        data = b"".join(chunks).decode(errors='ignore')

                        if '400 Bad Request' in data:
                            print(colored(
                                f"Received from port {port}: Request Error",
                                "red"
                            ))

                        else:
                            print(colored(
                                f"Received from port {port}:\n{data[:500]}",
                                "grey"
                            ))

                    except Exception as e:
                        print(colored(
                            f"Error sending HTTP request to port {port}: {e}",
                            "red"
                        ))

    # Handle exceptions for socket connection
    except socket.timeout:
        print(colored(f"Socket timeout on port {port}", "yellow"))
    except socket.error as err:
        print(colored(f"Socket error on port {port}: {err}", "yellow"))
    except Exception as e:
        print(colored(f"Error scanning port {port} on {host}: {e}", "red"))


# Main function to start the scanning process
def main():
    host = input(colored("[*] Enter the IP address to scan: ", "magenta"))
    if not validate_ip(host):
        print(colored("[!] Invalid IP address", "red"))
        return

    # Initialize the nmap scanner
    nm = nmap.PortScanner()
    open_ports = set()

    # List of common ports to scan
    common_ports = [
        21, 22, 23, 25, 53, 80, 110, 111, 123, 135,
        136, 137, 138, 139, 143, 161, 179, 389, 443, 444,
        445, 465, 513, 514, 546, 547, 548, 587, 591, 631,
        636, 853, 873, 902, 990, 993, 995, 1194, 1433, 1521,
        1701, 1723, 1812, 1813, 2049, 2082, 2083, 2087, 2095, 2096,
        3306, 3389, 4662, 4672, 5000, 5060, 5061, 5222, 5400, 5432,
        5500, 5800, 5900, 5938, 6660, 6661, 6662, 6664, 6665, 6666,
        6667, 6668, 6669, 6881, 6969, 8080, 8081, 8443, 10000, 5426
    ]

    # Create threads for each port to be scanned
    threads = [
        threading.Thread(target=scan_port, args=(host, port, open_ports, nm))
        for port in common_ports
    ]

    # Start each thread
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    while any(thread.is_alive() for thread in threads):
        for i in range(4):
            time.sleep(0.6)
            sys.stdout.write(colored(f"\r{' ' * i}", "blue"))
            sys.stdout.flush()

    # Join all threads
    for thread in threads:
        thread.join()

    # Print the final results
    print(colored("\n[*] Scan complete.", "green"))
    total_time = time.time() - start_time
    print(colored(f"Total execution time: {total_time:.2f} seconds", 'grey'))


# Entry point of the script
if __name__ == "__main__":
    main()
