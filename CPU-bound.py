from hashlib import md5
from random import choice
import concurrent.futures


def single_process():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)


#single_process()


def find_coins():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)


def main():
    max_workers = int(input("Введите число процессоров: "))
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        for i in range(1, max_workers + 1):
            executor.submit(find_coins, i)


if __name__ == '__main__':
    main()
