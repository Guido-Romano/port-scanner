
# Port Scanner

A simple Python-based port scanner that uses threading and Nmap to scan open ports and detect services.

## Features

- **Multi-threaded scanning**: Scans ports concurrently using Python's `threading` module.
- **Service detection**: Uses Nmap to detect services and their versions running on open ports.
- **Timeout handling**: Manages socket timeouts to ensure accurate results.
- **HTTP request to common web server ports**: Sends an HTTP request to check responses from common web server ports.

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
3. **Port Scanning**: The script concurrently scans a list of common ports on the host.
4. **Service Detection**: If a port is open, the script uses Nmap to detect the service, version, product, and extra info running on the port.
5. **HTTP Request**: For common web server ports (80, 443, 8080, 5426), the script sends an HTTP request and prints the response.
6. **Output**: The script prints the status of each scanned port, including open ports and detected services.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This project was inspired by the need to have a simple yet efficient port scanner using Python.

Special thanks to the developers of the Nmap and `termcolor` libraries.

