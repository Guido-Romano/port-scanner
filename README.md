
# Port Scanner

A simple Python-based port scanner that uses threading and Nmap to scan open ports and detect services on a given host.

## Features

- **Multi-threaded scanning**: Scans ports concurrently using Python's `threading` module.
- **Service detection**: Uses Nmap to detect services and their versions running on open ports.
- **Timeout handling**: Manages socket timeouts to ensure accurate results.

## Requirements

- Python 3.x
- `socket` (built-in)
- `termcolor` (install via pip)
- `threading` (built-in)
- `ipaddress` (built-in)
- `nmap` (install via pip)
- `tqdm` (install via pip)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/port-scanner.git
   cd port-scanner
