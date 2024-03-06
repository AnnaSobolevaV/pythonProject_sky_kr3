import json
from operator import itemgetter


def load_data(file_json):
    """
    Загружает данные из файла json
    """
    if file_json != '':
        with open(file_json) as file:
            data = json.load(file)
        return data


def get_dates_list(data):
    """
    Создает список значений по полям 'id' и 'date'
    для непустых записей и состоянием транзакции 'EXECUTED'
    """
    dates_list = []
    for item in data:
        if item != {} and item.get('state') == 'EXECUTED':
            dates_list.append([item.get('id'), item.get('date')])
    return dates_list


def build_total_list(data):
    """
    Возвращает список 5ти последних транзакций
    """
    # сортируем по дате
    dates_list = get_dates_list(data)
    sorted_list = sorted(dates_list, key=itemgetter(1), reverse=True)

    # итоговый список
    transactions_list = []
    for list_item in sorted_list[0:5]:
        for data_item in data:
            if data_item.get('id') == list_item[0]:
                transactions_list.append(data_item)
    return transactions_list


def str_formatted(str_):
    """
     - для Номера карты
    формирует строку формата XXXX XX** **** XXXX
    (видны первые 6 цифр и последние 4,
    разбито по блокам по 4 цифры, разделенных пробелом).
     - для Номер счета формирует строку формата **XXXX
    (видны только последние 4 цифры номера счета).
    """
    str_num = ''
    str_char = ''
    for symbol in str_:
        if symbol.isdigit():
            str_num += symbol
        else:
            str_char += symbol
    if 'Счет' in str_char:
        return str_char + '**' + str_num[-4:]
    else:
        return str_char + str_num[:4] + ' ' + str_num[4:6] + '** **** ' + str_num[-4:]


def date_str_formatted(date_str):
    """
    для Даты формирует строку формата ДД.ММ.ГГГГ
    """
    return date_str[8:10]+'.'+date_str[5:7]+'.'+date_str[:4]


def print_list(list_tr):
    """
    выводит на печать данные в формате
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>
    """
    for item in list_tr:
        from_str = ""
        if 'from' in item.keys():
            from_str = str_formatted(item['from'])
        to_str = str_formatted(item['to'])
        date_str = date_str_formatted(item['date'])
    return f""" {date_str} {item['description']}
{from_str} -> {to_str}
{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n
"""