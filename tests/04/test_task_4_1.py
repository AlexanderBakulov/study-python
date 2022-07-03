import pytest

from exercises.data_structures.task_4_1 import task_4_1


def test_task_4_1_success():
    test_nat = "ip nat inside source list ACL interface GigabitEthernet0/1 overload"
    assert task_4_1() == test_nat

def test_task_4_1_wrong():
    test_nat = "wrong string"
    assert task_4_1() != test_nat