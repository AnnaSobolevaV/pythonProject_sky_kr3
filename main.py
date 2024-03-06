from utils.functions import load_data
from utils.functions import build_total_list
from utils.functions import print_list

DATA_PATH = "./data/operations.json"


def main():
    data = load_data(DATA_PATH)
    print(data)
    list_transactions = build_total_list(data)
    print_list(list_transactions)


if __name__ == '__main__':
    main()
