from utils import functions
import pytest


def test_load_data():
    assert functions.load_data('') == None
    assert functions.load_data('./tests/test.json') == [
        {'id': 441945886, 'state': 'EXECUTED',
         'date': '2019-08-26T10:50:58.294041',
         'operationAmount': {'amount': '31957.58',
                             'currency': {'name': 'руб.', 'code': 'RUB'}
                             }
         }
    ]


@pytest.fixture
def test_data1():
    return [
        {'id': 441945886, 'state': 'EXECUTED',
         'date': '2019-08-26T10:50:58.294041',
         'operationAmount': {'amount': '31957.58',
                             'currency': {'name': 'руб.', 'code': 'RUB'}
                             }
         }
    ]


@pytest.fixture
def test_data2():
    return [
        {'id': 441945886, 'state': '',
         'date': '2019-08-26T10:50:58.294041',
         'operationAmount': {'amount': '31957.58',
                             'currency': {'name': 'руб.', 'code': 'RUB'}
                             }
         }
    ]


@pytest.fixture
def test_data3():
    return [
        {}
    ]


@pytest.fixture
def test_data4():
    return [
        {'id': 441945886, 'state': 'EXECUTED',
         'date': '2019-08-25T10:50:58.294041',
         'operationAmount': {'amount': '33.58',
                             'currency': {'name': 'руб.', 'code': 'RUB'}
                             }
         },
        {'id': 441945887, 'state': 'EXECUTED',
         'date': '2019-08-26T10:50:58.294041',
         'operationAmount': {'amount': '44.58',
                             'currency': {'name': 'руб.', 'code': 'RUB'}
                             }
         }
    ]


@pytest.fixture
def test_data5():
    return [
        {'id': 441945887, 'state': 'EXECUTED',
         'date': '2019-08-26T10:50:58.294041',
         'operationAmount': {'amount': '44.58',
                             'currency': {'name': 'руб.', 'code': 'RUB'}
                             }
         },
        {'id': 441945886, 'state': 'EXECUTED',
         'date': '2019-08-25T10:50:58.294041',
         'operationAmount': {'amount': '33.58',
                             'currency': {'name': 'руб.', 'code': 'RUB'}
                             }
         }
    ]


@pytest.fixture
def test_data6():
    return [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]


@pytest.fixture
def test_data7():
    return ('26.08.2019 Перевод организации \n'
 'Maestro 1596 83** **** 5199 -> Счет **9589\n'
 '31957.58 руб.\n'
 '\n')


@pytest.fixture
def test_data8():
    return [
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }]


@pytest.fixture
def test_data9():
    return ('23.03.2018 Открытие вклада \n -> Счет **2431\n48223.05 руб.\n\n')


def test_get_dates_list(test_data1, test_data2, test_data3):
    assert functions.get_dates_list(test_data1) == [[441945886, '2019-08-26T10:50:58.294041']]
    assert functions.get_dates_list(test_data2) == []
    assert functions.get_dates_list(test_data3) == []


def test_build_total_list(test_data4, test_data5):
    assert functions.build_total_list(test_data4) == test_data5


def test_str_formatted():
    assert functions.str_formatted("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert functions.str_formatted("Счет 35383033474447895560") == "Счет **5560"


def test_date_str_formatted():
    assert functions.date_str_formatted('2019-08-26T10:50:58.294041') == '26.08.2019'


def test_print_list(test_data6, test_data7, test_data8, test_data9):
    assert functions.print_list(test_data6) == test_data7
    assert functions.print_list(test_data8) == test_data9
