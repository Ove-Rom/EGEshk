from ipaddress import *

for a in range(255, -1, -1):
    net = ip_network(f"223.167.{a}.167/255.255.255.192", False)
    if all(f"{int(i):032b}"[:17].count("0") <= f"{int(i):032b}"[17:].count("0") for i in net):
        print(a)
        break