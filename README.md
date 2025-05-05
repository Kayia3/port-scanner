# Port Scanner
A multithreaded Python port scanner that scans a range of TCP ports on a given target host and saves the results in JSON or CSV format. 
It supports threading for faster scans and outputs detailed scan metadata including duration and common services.

# Features:
 -multithreaded scanning with ThreadPoolExecutor
 -customizable port range and thread count
 -outputs results in JSON or CSV format
 -measures and reports scan duration
 -Timestamped result file

# Tech
This project is build using the following techologies and Python libraies
- Python 3.x: The core programming language used for development.
- argparse: Python library for parsing command-line arguments.
- socket: Python library for low-level network programming.
- ThreadPoolExecutor: Python library for multiprocessing.
- json: Python library for working with JSON data.
- csv: Python library for working with csv data

## Command Line Options
```
python port_scanner.py --target <host> [options]
```
- -t, --target	Target IP or domain name (required)	
- -sp, --start-port	Start of port range	(default 1)
- -ep, --end-port	End of port range	(default 1024)
- -th, --threads	Number of scanning threads	(default 100)
- -f, --format	Output format: json or csv	(Default json)

Usage:
```
python port_scanner.py -t scanme.nmap.org -sp 20 -ep 100 -th 50 -f csv

