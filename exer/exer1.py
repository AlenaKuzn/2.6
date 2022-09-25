#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Список классов
    school = {'1a': 24, '2a': 18, '3a': 22, '6b': 17}

    print("Классы и количество учеников: ", school)

    # Изменения
    school['1a'] = 25
    school['1b'] = 20
    del school['2a']

    print("Классы и количество ученикв: ", school)
    print("Количество учеников в школе: ", sum(school.values()))
