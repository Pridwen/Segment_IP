import ipaddress
ip_net = '192.102.72.0'
print ('.'.join([bin(int(x)+256)[3:] for x in ip_net.split('.')]))