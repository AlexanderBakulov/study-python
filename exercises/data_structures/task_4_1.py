# -*- coding: utf-8 -*-
"""
Задание 4.1

Используя подготовленную строку nat, получить новую строку, в которой в имени
интерфейса вместо FastEthernet написано GigabitEthernet.
Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.

"""
import pytest



def task_4_1():
    nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
    print(nat.replace('Fast', 'Gigabit'))
    return nat.replace('Fast', 'Gigabit')


task_4_1()
