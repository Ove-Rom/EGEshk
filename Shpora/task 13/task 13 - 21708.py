from ipaddress import *

print(max(ip_network("11.92.135.56/255.224.0.0", False).hosts()))