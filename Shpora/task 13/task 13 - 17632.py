from ipaddress import *

net = ip_network("112.160.0.0/255.240.0.0", False)
ans = 0

for i in net:
    s = f"{int(i):032b}"
    ans += s.count("1") % 5 == 0

print(ans)