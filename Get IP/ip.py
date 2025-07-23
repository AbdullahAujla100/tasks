import socket 

website="www.google.com"

ip=socket.gethostbyname(website)
hostinfo=socket.gethostbyaddr(ip)[0]

print(f"website name: {website}")
print(f"ip-address: {ip}")
print(f"host_info: {hostinfo}")