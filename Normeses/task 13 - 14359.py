from ipaddress import *

for mask in range(33):
    n1 = ip_network(f"157.127.172.56/{mask}", 0)
    n2 = ip_network(f"157.127.191.78/{mask}", 0)
    if n1 != n2:
        print(mask)
        break
