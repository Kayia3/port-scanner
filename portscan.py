import datetime
import socket
import json
import csv
import argparse
from concurrent.futures import ThreadPoolExecutor,as_completed

common_ports = {
    21: 'FTP', 22: 'SSH', 23: 'Telnet', 25:'SMTP',
    53: 'DNS', 80: 'HTTP', 110: 'POP3', 143: 'IMAP',
    443: 'HTTPS', 3306: 'MySQL', 3389: 'RDP'
}

open_ports = []

#argument parsing
parser = argparse.ArgumentParser(description="Advanced Port Scanner with Output Format and Timestamp")
parser.add_argument('-t',"--target",required=True,help="Target IP or hostname")
parser.add_argument('-sp',"--start-port",type = int,default=1,help="Start of port range")
parser.add_argument('-ep',"--end-port",type = int,default=1024,help="End of port range")
parser.add_argument('-th',"--threads",type=int,default=100,help="Number of scanning threads")
parser.add_argument('-f',"--format",choices=["json","csv"],default="json",help="Output format: json or csv")
args = parser.parse_args()

target = args.target
port_range = range(args.start_port, args.end_port + 1)
thread_count = args.threads
output_format = args.format

#port scan
def scan_port(port,Target):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((Target,port))

            if result == 0:
                service = common_ports.get(port,"Unknown")
                print(f"Port {port} open ({service})")
                return{"port": port, "service":service}
            
    except Exception:
        pass
    return None

def output_file_format(output_format,filename,duration):
    if output_format == "json":
        output = {
            "target":target,
            "scan_range": f"{args.start_port}-{args.end_port}",
            "scan_duration_seconds": round(duration,2),
            "open_ports": open_ports
        }
        with open(filename, "w") as f:
            json.dump(output,f, indent=4)
    elif output_format == "csv":
        with open(filename, "w") as f:
            writer = csv.DictWriter(f, fieldnames=["port","service"])
            writer.writeheader()
            for entry in open_ports:
                writer.writerow(entry)

def main():
    

    print(f"\nScanning {target} ports { args.start_port}-{args.end_port} with {thread_count} threads ...\n")


    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        futures = {executor.submit(scan_port,port): port for port in port_range}
        for future in as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)
                
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    filename = f"scan_{timestamp}.{output_format}"

    output_file_format(output_format,filename)
    

    print(f"\nSaved in {filename}")

main()