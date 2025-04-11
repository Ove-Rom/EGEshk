from ipaddress import *
from tqdm import tqdm

net = ip_network("115.192.0.0/255.192.0.0")

c = 0

for ip in tqdm(net):
    ip = f"{int(ip):032b}"
    if ip.count("1") % 3: c += 1

print(c)