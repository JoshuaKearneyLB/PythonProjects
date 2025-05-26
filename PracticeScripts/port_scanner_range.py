import socket
import time
import random
#Using random means probes are not blocked by router
RED='\033[91m'
GREEN='\033[92m'
RESET='\033[0m'

 #Function to scan host and port range (Host, portStart, portEnd)
def port_scan_range(host, portStart, portEnd):

    openPorts = []

    print(f"Scanning {host} from port {portStart} to {portEnd}...")
    for port in range(portStart, portEnd + 1):
        try:
            # Create a socket object (IPv4, TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f"Created socket: {s}")

            #Set a timeout for socket
            s.settimeout(2)
            print(f"Timeout set to {s.gettimeout()} seconds")
    
            print(f"Attempting to connect to {host}:{port}...")
            result = s.connect_ex((host, port))  # Returns 0 if successful
            if result == 0:
                print(f"{GREEN}[+] Connection successful to {host}:{port}{RESET}")
            else:
                print(f"{RED}[-] Port {port} is closed or filtered (code: {result}){RESET}")
        except socket.gaierror:
            print("[!] Hostname could not be resolved")
        except socket.error as err:
            print(f"[!] Socket error: {err}")
        time.sleep(random.randint(1,4))

        # Close the socket
        s.close()
        print("Socket closed.")

port_scan_range('192.168.0.1', 53, 80)