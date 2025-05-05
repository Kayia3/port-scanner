# Port Scanner
A multithreaded Python port scanner that scans a range of TCP ports on a given target host and saves the results in JSON or CSV format. 
It supports threading for faster scans and outputs detailed scan metadata including duration and common services.

Features: 
 -multithreaded scanning with ThreadPoolExecutor
 -customizable port range and thread count
 -outputs results in JSON or CSV format
 -measures and reports scan duration
 -Timestamped result file

Command Line Options
bash: 
python port_scanner.py --target <host> [options]

-t, --target	Target IP or domain name (required)	
-sp, --start-port	Start of port range	(default 1)
-ep, --end-port	End of port range	(default 1024)
-th, --threads	Number of scanning threads	(default 100)
-f, --format	Output format: json or csv	(Default json)

ex:
python port_scanner.py -t scanme.nmap.org -sp 20 -ep 100 -th 50 -f csv

