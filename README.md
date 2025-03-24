# Python Port Scanner v1.0

A Python-based port scanner designed for efficient scanning of all ports using threading and socket libraries.

## Features

- **Multi-threaded Scanning**: Leverages Python's `threading` module to scan ports concurrently, ensuring faster results.
- **Timeout Management**: Configures socket timeouts for optimized and accurate port scanning.
- **Simple and Effective**: Focused on functionality and speed, scanning all ports on a specified target host.

## Requirements

- Python 3.x
- `socket` (built-in)
- `threading` (built-in)

## Installation & Use

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/python-port-scanner
    cd python-port-scanner
    ```

2. **Run the script**:

    ```bash
    python3 port_scanner.py
    ```

## How It Works

1. **Input**: The user is prompted to enter the IP address of the target host.
2. **Port Scanning**: The script scans all ports (from 1 to 65535) using multi-threading to enhance speed.
3. **Output**: Open ports are displayed, and error messages are handled gracefully.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Special thanks to Python's `socket` and `threading` libraries for making port scanning straightforward and efficient.

Special thanks to the developers of the Nmap and `termcolor` libraries.



