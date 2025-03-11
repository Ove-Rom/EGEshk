from ipaddress import ip_network

ans = []

for mask in range(33):
    net1 = ip_network(f"10.96.180.231/{mask}", 0)
    net2 = ip_network(f"10.96.140.118/{mask}", 0)
    if net1.network_address != net2.network_address and\
        bin(int(net1.netmask))[2:].count('1') == bin(int(net2.netmask))[2:].count('1'):
        ans.append(bin(int(net1.netmask))[2:].count('0'))

print(max(ans))