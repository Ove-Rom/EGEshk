from ipaddress import *

net = ip_network("112.160.0.0/255.240.0.0")

c = 0

for ip in net:
    ip = f"{int(ip):032b}"
    if ip.count('1') % 3: c += 1

print(c)