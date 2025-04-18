from ipaddress import *

net = ip_network("192.168.31.80/255.255.255.240")
ans = []

for i in net:
    s = f"{int(i):032b}"
    ans.append(s.count("1"))

print(max(ans))