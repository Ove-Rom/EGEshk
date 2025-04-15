from ipaddress import *

net = ip_network("214.187.224.0/255.255.224.0", False)

c = 0

for i in net:
    s = f"{int(i):032b}"
    c1 = s.count("1") % 6
    c2 = s[-4:] == "1000"
    if c1 and c2:
        c += 1

print(c)