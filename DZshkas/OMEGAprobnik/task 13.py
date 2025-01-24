from ipaddress import *

for i in range(33):
    print(ip_network(f"203.155.64.98/{i}", 0))