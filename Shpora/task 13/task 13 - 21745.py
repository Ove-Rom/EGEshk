from ipaddress import *

from tqdm import tqdm

ip1 = ip_address("95.24.2.9")
ip2 = ip_address("95.24.3.10")
ans = []

for mask in tqdm(range(10, 31)):
    net1 = ip_network(f"{ip1}/{mask}", False)
    net2 = ip_network(f"{ip2}/{mask}", False)
    if ip1 in net1.hosts() and ip2 in net2.hosts():
        c = 0
        if net1 != net2:
            for i in net1.hosts():
                s = f"{int(i):032b}"
                c += s[-1] == "0"
            ans.append(c)

print(max(ans))