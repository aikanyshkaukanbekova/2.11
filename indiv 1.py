#!/usr/bin/env python3
# _*_ coding: utf-8 -*-

def fun1(type_='max'):
    def fun2(lst):
        if type_ == 'max':
            return max(lst)
        elif type_ == 'min':
            return min(lst)
    print(type_)
    return fun2


if __name__ == '__main__':
    a = [1, 2, 34, 54, 36, 7, 8]
    max_fun = fun1()
    min_fun = fun1('min')
    print(max_fun(a))
    print(min_fun(a))
