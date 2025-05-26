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
target_host = str(input("Enter host: "))
target_port = int(input("Enter Port: "))

try:
    print(f"Attempting to connect to {target_host}:{target_port}...")
    result = s.connect_ex((target_host, target_port))  # Returns 0 if successful

    if result == 0:
        print(f"{GREEN}[+] Connection successful to {target_host}:{target_port}{RESET}")
        try:
            service = socket.getservbyport(target_port)
            print(f"{GREEN}[+] Port {target_port} is open ({service}){RESET}")
            banner = s.recv(1024).decode().strip()
            if banner:
                print(f"{GREEN}[+] Banner: {banner}{RESET}")
            else:
                print(f"{GREEN}[+] Port {target_port} is open - No banner received{RESET}")
        except:
            "UNKNOWN SERVICE"
    else:
        print(f"{RED}[-] Port {target_port} is closed or filtered (code: {result}){RESET}")
except socket.gaierror:
    print("[!] Hostname could not be resolved")
except socket.error as err:
    print(f"[!] Socket error: {err}")

# Close the socket
s.close()
print("Socket closed.")
