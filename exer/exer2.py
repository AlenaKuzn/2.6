#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Создание словря
    slovar = {1: 'hel', 2: 'hol', 3: 'hil'}

    # Применение метода items
    print(slovar.items())
    # Создание обратного словоря
    print({value:key for key, value in slovar.items()})
