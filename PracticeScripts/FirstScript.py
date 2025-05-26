import socket

def grab_banner(host, port):
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((host, port))

        # For HTTP ports, send a request to trigger a banner
        if port == 80:
            s.send(b"HEAD / HTTP/1.1\r\nHost: " + bytes(host, "utf-8") + b"\r\n\r\n")

        banner = s.recv(1024)
        print(f"[+] Banner from {host}:{port}:\n{banner.decode(errors='ignore').strip()}")
        s.close()
    except socket.timeout:
        print(f"[-] {host}:{port} - Connection timed out")
    except Exception as e:
        print(f"[-] Failed to grab banner from {host}:{port} — {e}")

# Example usage:
grab_banner("scanme.nmap.org", 21)
grab_banner("scanme.nmap.org", 80)


