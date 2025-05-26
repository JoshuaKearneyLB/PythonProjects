
import socket
RED='\033[91m'
GREEN='\033[92m'
RESET='\033[0m'


# Create a socket object (IPv4, TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Created socket: {s}")

# Set a timeout (so it doesn't hang forever)
s.settimeout(3)
print(f"Timeout set to: {s.gettimeout()} seconds")

# Try connecting using socket

target_host = str(input("Enter IP: "))
target_port = int(input("Enter Port: "))

try:
    print(f"Attempting to connect to {target_host}:{target_port}...")
    result = s.connect_ex((target_host, target_port))  # Returns 0 if successful
    if result == 0:
        print(f"{GREEN}[+] Connection successful to {target_host}:{target_port}{RESET}")
    else:
        print(f"{RED}[-] Port {target_port} is closed or filtered (code: {result}){RESET}")
except socket.gaierror:
    print("[!] Hostname could not be resolved")
except socket.error as err:
    print(f"[!] Socket error: {err}")

# Close the socket
s.close()
print("Socket closed.")
