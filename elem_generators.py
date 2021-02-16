import random
import time
import sys


class CongruentGenerator():
    def __init__(self):
        pass


class FibonacciGenerator():
    def __init__(self):
        pass


# получение параметров
def get_param(choice: int):
    print("Choose where to set parameters (initial state, sequence length):\n\t1. File\n\t2. Manually")
    c = int(input())
    if c == 1:
        print("input name file with param: ")
        filename = input()
        try:
            with open(filename, "r") as file:
                init_state = file.readline().rstrip('\n').split(' ')
                init_state = [int(el) for el in init_state]
                len_sequence = int(file.readline())
                return init_state, len_sequence
        except FileNotFoundError:
            print("[!] file with this name does not exist")
    elif c == 2:
        print("Input init_state (x_0 or init sequence): ")
        init_state = input().rstrip('\n').split(' ')
        init_state = [int(el) for el in init_state]
        print("Enter the length of the sequence: ")
        len_sequence = int(input())
        return init_state, len_sequence
    else:
        print("[!] Error input init param ...")


# начало считывания параметров (вернуть объект класса)
def start_get_param():
    print("Choose which generator to run:\n\t1. Congruent Generator\n\t2. Fibonacci Generator")
    choice = int(input())
    if choice == 1:
        init_state, len_sequence = get_param(choice)
    elif choice == 2:
        init_state, len_sequence = get_param(choice)
    else:
        print("[!] Error input parameters, try again ...")
        sys.exit()

    print("How to set generator parameters:\n\t1. Automatic generation\n\t2. Manually")
    param = int(input())
    if param == 1:
        #  автоматическая генерация в зависимости от генератора
        if choice == 1:
            pass  # автоматическая генерация для конгруэнтного генератора
        else:
            pass  # автоматическая генерация для генератора Фибоначи
    elif param == 2:
        if choice == 1:
            # считывание параметров для генератора и инициализация объекта класса
            pass
        else:
            # считывание параметров для генератора фибоначи и инициализация объекта
            pass
    else:
        print("[!] Error input parameters for generators, try again ...")
        sys.exit()


if __name__ == "__main__":
    start_get_param()