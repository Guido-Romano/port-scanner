#!/usr/bin/env python3

import socket
from termcolor import colored
import threading
import ipaddress
import nmap
from tqdm import tqdm  # Asegurarse de importar correctamente

def validar_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def scan_port(host, port, pbar):
    nm = nmap.PortScanner()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2.0)  # Aumentar el tiempo de espera
            result = sock.connect_ex((host, port))
            if result == 0:
                # Pausar la barra de progreso
                pbar.clear()

                print(colored(f"[+] Port {port} open", "green"))

                # Detectar servicios y versiones usando nmap
                nm.scan(host, str(port), '-sV')
                service = nm[host]['tcp'][port]['name']
                version = nm[host]['tcp'][port]['version']
                product = nm[host]['tcp'][port]['product']
                extra_info = nm[host]['tcp'][port].get('extrainfo', '')

                print(colored(f"    Service: {service}", "blue"))
                print(colored(f"    Version: {version}", "blue"))
                print(colored(f"    Product: {product}", "blue"))
                if extra_info:
                    print(colored(f"    Extra Info: {extra_info}", "blue"))

                # Reanudar la barra de progreso
                pbar.refresh()

            if port in [80, 443, 8080, 5426]:
                mensaje = 'GET / HTTP/1.1\r\nHost: {}\r\nUser-Agent: Python-Scanner\r\nConnection: close\r\n\r\n'.format(host)
                sock.sendall(mensaje.encode())  # Enviar datos

                chunks = []
                while True:
                    chunk = sock.recv(1024)  # Recibir fragmento de datos
                    if not chunk:
                        break
                    chunks.append(chunk)
                data = b''.join(chunks)  # Unir todos los fragmentos

                # Pausar la barra de progreso
                pbar.clear()
                print(colored(f"Recibido del puerto {port}: {data}", "blue"))
                # Reanudar la barra de progreso
                pbar.refresh()

    except socket.timeout:
        print(colored(f"Socket timeout en el puerto {port}", "yellow"))
    except socket.error as err:
        print(colored(f"Socket error en el puerto {port}: {err}", "yellow"))
    except Exception as e:
        print(colored(f"Error scanning port {port} on {host}: {e}", "red"))
    finally:
        pbar.update(1)  # Actualizar la barra de progreso

def main():
    host = input("[*] Enter the IP address to scan: ")

    if not validar_ip(host):
        print(colored("[!] Dirección IP inválida", "red"))
        return

    # Crear un hilo por puerto
    ports = range(1, 5536)
    pbar = tqdm(total=len(ports), desc="Escaneando puertos")
    threads = [threading.Thread(target=scan_port, args=(host, port, pbar)) for port in ports]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    pbar.close()

main()




