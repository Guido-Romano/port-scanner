# Port Scanner

A highly aggressive Python-based port scanner designed to quickly and efficiently scan the 100 most common ports using threading and Nmap.

## Features

- **Aggressive Multi-threaded Scanning**: Scans ports concurrently using Python's `threading` module to achieve rapid results.
- **Service Detection**: Uses Nmap to detect services and their versions running on open ports.
- **Timeout Handling**: Manages socket timeouts to ensure accurate and swift results.
- **HTTP Request to Common Web Server Ports**: Sends an HTTP request to check responses from common web server ports (80, 443, 8080, 5426).

## Requirements

- Python 3.x
- `socket` (built-in)
- `termcolor` (install via pip)
- `threading` (built-in)
- `ipaddress` (built-in)
- `nmap` (install via pip)

## Installation & Use

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/port-scanner.git
    cd port-scanner
    ```

2. **Install the required packages**:

    ```bash
    pip install termcolor nmap
    ```

3. **Run the script and enter the IP address of the host you want to scan**:

    ```bash
    python port-scanner.py
    ```

## How It Works

1. **Input**: The script prompts the user to enter the IP address of the target host.
2. **Validation**: The IP address is validated to ensure it is in the correct format.
3. **Aggressive Port Scanning**: The script concurrently scans a list of the 100 most common ports on the host using multiple threads to speed up the process.
4. **Service Detection**: If a port is open, the script uses Nmap to detect the service, version, product, and extra info running on the port.
5. **HTTP Request**: For common web server ports (80, 443, 8080, 5426), the script sends an HTTP request and prints the response.
6. **Output**: The script prints the status of each scanned port, including open ports and detected services.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This project was inspired by the need to have a simple yet efficient and aggressive port scanner using Python.

Special thanks to the developers of the Nmap and `termcolor` libraries.



