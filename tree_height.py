import sys
import threading
import os
import numpy as np

c = 0


def aray(size, numbers):
    arr1 = np.zeros(size)
    k, start = 1, 0
    for a in range(size):
        arr1[a] = numbers[a]
        if arr1[a] == -1:
            start = a
    check(k, start, arr1)


def check(k, start, arr1):
    global c
    for a in range(arr1.size):
        if arr1[a] == start:
            move = a
            k += 1
            if c < k:
                c = k
            k = check(k, move, arr1)
    k -= 1
    return k


def main():
    first_input = input()
    if first_input.__contains__('I'):
        second_input = int(input())
        third_input = input()
        aray(second_input, third_input)
    elif first_input.__contains__('F'):
        file_name = input()
        if file_name.__contains__('a'):
            print("INPUT-OUTPUT ERROR")
            return
        file = os.path.join(os.getcwd(), 'test', file_name)
        with open(file, 'r') as f:
            second_input = int(f.readline())
            third_input = list(map(int, f.readline().strip().split()))
            aray(second_input, third_input)
    else:
        print("INPUT-OUTPUT ERROR")
        return
    print(c)


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
