import ipaddress
import sys
import math


if __name__ == '__main__':
    ip_net = sys.argv[1]
    chop = int(sys.argv[2])
    dummy = ip_net.split('/')
    auxiliarmus = dummy[1]
    net = ipaddress.ip_network(ip_net, strict=False)
    leap = net.num_addresses / chop
    lista = []
    counter = 0
    n = 0
    j = 1
    for ip in ipaddress.IPv4Network(ip_net, False):
        if counter == 0 or counter == net.num_addresses - 1:
            lista.append(ip)
            n = n + 1
        elif counter == (leap * n):
            lista.append(ip - 1)
            lista.append(ip)
            n = n + 1
        counter = counter + 1
    for i in range(len(lista)):
        if i % 2 == 0:
            print("Subretea", j)
            print("\tMin IP:", lista[i], "/", int(auxiliarmus) + int(math.log(chop, 2)))
            print("\tMax IP:", lista[i + 1], "/", int(auxiliarmus) + int(math.log(chop, 2)))
            print("\n")
            j = j + 1
