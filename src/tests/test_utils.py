import pytest
from src import utils

@pytest.fixture
def operations():
    return [
  {
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
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "CANCELLED",
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
  },
  {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  },
    ]

def test_remove_invalid(operations):
    assert utils.remove_invalid(operations) == [operations[1], operations[2], operations[4]]

def test_data_date(operations):
    assert sorted(operations, key=utils.data_date, reverse=True) == [operations[0], operations[1], operations[4], operations[2], operations[3]]


def test_remove_invalid_operations(operations):
    assert len(utils.remove_invalid(operations)) == 3

def test_data_date_operations(operations):

    sorted_data = sorted(operations, key=utils.data_date)
    assert sorted_data[0]['date'] == "2018-03-23T10:45:06.972075"
    assert sorted_data[-1]['date'] == "2019-08-26T10:50:58.294041"

def test_lastoper_operations(operations):
    data_corr = utils.remove_invalid(operations)

    assert utils.lastoper(data_corr, 1) == print("01.08.2021 Перевод организации\n123456****7890  ->  3210\n31957.58 RUB\n")
