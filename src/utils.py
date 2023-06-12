import json
import datetime
import os


dir_path = os.path.dirname(os.path.realpath(__file__))


with open(dir_path + '/' + 'operations.json', 'r') as file:
    data = json.load(file)


def remove_invalid(data):
    data_corr = []

    for i in data:
        if "date" in i.keys() and "state" in i.keys() and \
                "description" in i.keys() and "from" in i.keys() and "to" in i.keys() and i["state"] == 'EXECUTED' and i["from"]!= None:
            data_corr.append(i)
    return data_corr


def data_date(el):
    return el['date']


def lastoper(data_corr, count):
    data_corr.sort(key=data_date, reverse=True)

    for i in range(count):
        # print(data_corr[i]["date"])"
        formated_date = datetime.datetime.strptime(data_corr[i]["date"],"%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        descriptions = data_corr[i]["description"]
        type_card = data_corr[i]["from"]
        type_card_ = data_corr[i]["to"]
        masked_type_card_from = type_card[:-10] +"*" * 6 + type_card[-4:]
        masked_type_card_to = "*" * 2 + type_card_[-4:]
        summa_ = data_corr[i]["operationAmount"]["amount"]
        name_type = data_corr[i]["operationAmount"]["currency"]["name"]
        print(f"{formated_date} {descriptions}")
        print(f"{masked_type_card_from}  ->  {masked_type_card_to}")
        print(summa_, name_type)
        print()



if __name__ == '__main__':
    data_corr = remove_invalid(data)
    lastoper(data_corr, 5)