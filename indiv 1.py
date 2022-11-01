#!/usr/bin/env python3
# _*_ coding: utf-8 -*-

def fun1(type_='max'):
    def fun2(lst):
        return eval(f'{type_}(lst)')
    print(type_)
    return fun2


a = [1, 2, 34, 54, 36, 7, 8]

max_fun = fun1()
min_fun = fun1('min')

if __name__ == '__main__':
    print(max_fun(a))
    print(min_fun(a))