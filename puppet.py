import ipaddress
ip_net = '192.102.72.0/24'
chop = 4
dummy = ip_net.split('/')
auxiliarmus = dummy[1]
net = ipaddress.ip_network(ip_net, strict=False)
leap = net.num_addresses / chop
lista = []
print("Jump pattern", int(leap))
counter = 0
n = 0
for ip in ipaddress.IPv4Network(ip_net, False):
    if counter == 0 or counter == net.num_addresses-1:
        lista.append(ip)
        n = n + 1
    elif counter == (leap*n):
        lista.append(ip-1)
        lista.append(ip)
        n = n + 1
    counter = counter + 1
for i in range(len(lista)):
    print(lista[i], i)