from fractions import Fraction


def list_prod(l: list) -> Fraction:
    acc = 1
    for i in l:
        acc *= i
    return acc


def list_dot(l1: list, l2: list) -> Fraction:
    acc = 0
    for i in range(len(l1)):
        acc += l1[i]*l2[i]
    return acc


def list_add(l1: list, l2: list) -> list:
    l = list()
    for i in range(len(l1)):
        l.append(l1[i]+l2[i])
    return l