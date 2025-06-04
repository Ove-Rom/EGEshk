from ipaddress import *

net = ip_network("115.192.0.0/255.192.0.0", False)
ans = 0

for i in net:
    s = f"{int(i):032b}"
    ans += s.count("1") % 3 != 0

print(ans)