
import json

FILE = "input.csv"

'''
Функция конвертер из csv в json формат
:param filename: str
:return: list_dict: list
'''


def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename) as f: #читаем файл
        list = [] #задаем список
        for index, line in enumerate(f): #счетчик элементов
            u = line.strip(new_line).split(delimiter)
            if index == 0:
                headers = u
                continue
            list.append({}) #добавляем в конец списка
            for i, _ in enumerate(headers):
                 list[-1][headers[i]] = u[i]
    return list # возвращаем список

print(json.dumps(csv_to_list_dict(FILE), indent=4))
