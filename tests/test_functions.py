from utils import functions
import pytest

def test_load_data():
    assert functions.load_data('') == None
    assert functions.load_data('test.json') == [
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

def test_get_dates_list(test_data1, test_data2, test_data3):
    assert functions.get_dates_list(test_data1) == [[441945886, '2019-08-26T10:50:58.294041']]
    assert functions.get_dates_list(test_data2) == []
    assert functions.get_dates_list(test_data3) == []

def test_build_total_list(test_data4, test_data5):
    assert functions.build_total_list(test_data4) == test_data5