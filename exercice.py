#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


# TODO: Définissez vos fonction ici
def ex_01(a=1, b=2, c=3, m=4):
    v = 4/3 * (math.pi * a * b * c)
    mv = v * m
    return v, mv

def ex_02(sentence):
    keys = list(set(sentence))
    dic = {key: sentence.count(key) for key in keys if sentence.count(key) > 5}
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return dic


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    result = ex_01(c=5, m=10)
    print(result)

    sentence = "The fuck d'you say to me you little shit"
    print(ex_02(sentence))
