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

### Debian-based distributions (e.g., Ubuntu, Kali)

1. **Update package lists**:

    ```bash
    sudo apt-get update
    ```

2. **Install Python**:

    ```bash
    sudo apt-get install python3
    ```

3. **Run the script**:

    ```bash
    python3 port-scanner.py
    ```

### Arch-based distributions (e.g., Arch Linux, BlackArch)

1. **Update package lists**:

    ```bash
    sudo pacman -Syu
    ```

2. **Install Python**:

    ```bash
    sudo pacman -S python
    ```

3. **Run the script**:

    ```bash
    python3 port-scanner.py
    ```

### Red Hat-based distributions (e.g., CentOS, Fedora)

1. **Update package lists**:

    ```bash
    sudo dnf update
    ```

2. **Install Python**:

    ```bash
    sudo dnf install python3
    ```

3. **Run the script**:

    ```bash
    python3 port-scanner.py
    ```

### How It Works

1. **Input**: The user is prompted to enter the IP address of the target host.
2. **Port Scanning**: The script scans all ports (from 1 to 65535) using multi-threading to enhance speed.
3. **Output**: Open ports are displayed, and error messages are handled gracefully.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Special thanks to Python's `socket` and `threading` libraries for making port scanning straightforward and efficient.
