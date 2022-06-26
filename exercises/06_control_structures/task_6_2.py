# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_addr = input("Imput IP address: ")
ip_addr_octets = ip_addr.split('.')
if ip_addr_octets[0] == '0' and ip_addr_octets[1] == '0' and ip_addr_octets[2] == '0' and ip_addr_octets[3] == '0':
    print('unassigned')
elif ip_addr_octets[0] == '255' and ip_addr_octets[1] == '255' and ip_addr_octets[2] == '255' and ip_addr_octets[3] == '255':
    print('local broadcast')
elif 0 < int(ip_addr_octets[0]) < 224:
    print('unicast')
elif 224 <= int(ip_addr_octets[0]) <= 239:
    print('multicast')
else:
    print('unused')
