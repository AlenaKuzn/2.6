#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date

if __name__ == '__main__':
    # Список рейсов.
    reys = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о рейсе.
            pynkt = input("Пункта назначения рейса: ")
            numb = int(input("Номер рейса: "))
            samolet = input("Тип самолета: ")

            # Создать словарь.
            rey = {
                'pynkt': pynkt,
                'numb': numb,
                'samolet': samolet,
                }

            # Добавить словарь в список.
            reys.append(rey)

            # Отсортировать список в случае необходимости.
            if len(reys) > 1:
                reys.sort(key=lambda item: item.get('numb', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,

                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "No",
                "Пункт назначения",
                "Номер рейса",
                "Тип"
                )
            )
            print(line)

            # Вывести данные о всех рейсах.
            for idx, rey in enumerate(reys, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    rey.get('pynkt', ''),
                    rey.get('numb', ''),
                    rey.get('samolet', 0)
                    )
                )
                print(line)

        elif command.startswith('select '):
            # Разбить команду на части.
            parts = command.split(' ', maxsplit=1)
            # Получить требуемый город.
            pynkt_pr = str(parts[1])

            count = 0

            # Проверить сведения о пункте.
            for rey in reys:
                if rey.get('pynkt','') == pynkt_pr:
                    count += 1
                    print("Номер рейса: ",
                        rey.get('numb'),
                        "Тип самолета: ",
                        rey.get('samolet'))
                    count += 1
            if count == 0:
                print("В данный пункт самолетов нет.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("select <стаж> - запросить работников со стажем;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
