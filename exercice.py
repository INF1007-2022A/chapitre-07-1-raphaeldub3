#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


# TODO: Définissez vos fonction ici
def masse_volume(a=1, b=2, c=3, m=4):
    V = 4/3 * math.pi * a * b * c
    mV = V * m
    return V, mV


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    result = masse_volume(c=5, m=10)
    print(result)
