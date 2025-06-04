from ipaddress import *

for a in range(1_000):
    net = ip_network(f"192.214.{a}.184/255.255.255.224", False)
    if all(sum(map(int, f"{int(i):b}")) > 15 for i in net):
        print(a)
        break
