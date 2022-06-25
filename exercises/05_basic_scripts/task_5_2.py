# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
prefix = input('Input ip and mask (example 10.1.1.12/24): ')
prefix_list = prefix.split('.')
mask = prefix_list[3][-3:]
prefix_list[3] = '0'
ip_addr_1 = f'{int(prefix_list[0]):<10}{int(prefix_list[1]):<10}{int(prefix_list[2]):<10}{int(prefix_list[3]):<10}'
ip_addr_2 = '{:08b}  {:08b}  {:08b}  {:08b}'.format(int(prefix_list[0]), int(prefix_list[1]), int(prefix_list[2]), int(prefix_list[3]))
mask_bin = '1'*int(mask[1:]) + '0'*(32 - int(mask[1:]))
mask_dec = f'{int(mask_bin[0:8],2):<10}{int(mask_bin[8:16], 2):<10}{int(mask_bin[16:24], 2):<10}{int(mask_bin[24:32], 2):<10}'
mask_bits = f'{mask_bin[0:8]}  {mask_bin[8:16]}  {mask_bin[16:24]}  {mask_bin[24:32]}'



print('Network:')
print(ip_addr_1)
print(ip_addr_2 + '\n')
print('Mask:')
print(mask)
print(mask_dec)
print(mask_bits)
