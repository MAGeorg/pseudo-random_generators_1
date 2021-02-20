import random
import time
import sys
from math import sqrt
from itertools import count, islice


class CongruentGenerator:
    def __init__(self, x_0, c0=None, a=None, N=None, cnt=128):
        self.x_0 = x_0[0]
        self.cnt = cnt
        self.c_0 = int()
        self.a = int()
        self.N = int()
        if c0 == None and a == None and N == None:
            flag = True
            while flag:
                try:
                    self.c_0, self.a, self.N = self.__generate_param()
                    flag = False
                except:
                    print("[*] Unsuccessful generation, trying again ... ")
            print("------------------------------------------------------")
            print("--------------- Generated parameters -----------------")
            print("\tx0 = {}\n\tc0 = {}\n\ta = {}\n\tN = {}".format(self.x_0, self.c_0, self.a, self.N))
            print("------------------------------------------------------\n")
        else:
            self.c_0 = c0
            self.a = a
            self.N = N

    # генерация параметров
    def __generate_param(self):
        q_list = [8, 16, 32] #, 64]
        q = random.choice(q_list)
        st = time.time()
        c0 = random.randint(1000, 10000)
        N = 2 ** q
        for a in range(10000):
            if is_prime(a * N - 1) and is_prime((a * N - 2)/2):
                print("Parameter generation time  (in sec): {}".format(time.time() - st))
                return c0, a, N
        else:
            raise

    def __print_seq_to_file(self, seq: list):
        with open('result.txt', 'w') as fl:
            for el in seq:
                fl.write('%i\n' % el)

    def generate_sequence(self, x_0, c_0, a, N, cnt):
        # print(x_0,c_0,a,N, cnt)
        seq = [x_0]
        st = time.time_ns()
        for i in range(cnt - 1):
            x_0 = (a * x_0 + c_0) % N
            c_0 = int((a * x_0 + c_0) / N)
            seq.append(x_0)
        end = time.time_ns()
        # print(st,'\n', end)
        print("Generator running time (in nsec): {}".format(end - st))
        self.__print_seq_to_file(seq)


class FibonacciGenerator:
    def __init__(self):
        pass


# проверка на простоту
def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


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
            cong_obj = CongruentGenerator(init_state, cnt=len_sequence)
            return cong_obj
        else:
            pass  # автоматическая генерация для генератора Фибоначи
    elif param == 2:
        if choice == 1:
            print("Enter parameters: ")
            c0 = int(input("Enter c0 << "))
            a = int(input("Enter a << "))
            N = int(input("Enter N << "))
            cong_obg = CongruentGenerator(init_state, c0, a, N, len_sequence)
            return cong_obg
        else:
            # считывание параметров для генератора фибоначи и инициализация объекта
            pass
    else:
        print("[!] Error input parameters for generators, try again ...")
        sys.exit()


if __name__ == "__main__":
    cong_obg = start_get_param()
    cong_obg.generate_sequence(cong_obg.x_0, cong_obg.c_0, cong_obg.a, cong_obg.N, cong_obg.cnt)

    print("\n\nПараметры что были считаны: x0, c0, a, N, cnt")
    print(cong_obg.x_0, cong_obg.c_0, cong_obg.a, cong_obg.N, cong_obg.cnt)


