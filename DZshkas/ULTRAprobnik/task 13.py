from ipaddress import *

count = 0

for ip in ip_network("101.157.240.0/255.255.252.0"):
    base = f"{ip:b}"
    cl = sum(int(i) for i in base[:16])
    cr = sum(int(i) for i in base[16:])
    if cl > cr: count += 1

print(count)