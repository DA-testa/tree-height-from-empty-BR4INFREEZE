import sys
import threading
import os
import numpy as np

c = 0


def aray(size, numbers):

    global c
    arr1 = np.zeros(size)
    for a in range(size):
        k = check(a, numbers, arr1)
        if c < k:
            c = k


def check(a, numbers, arr1):

    if arr1[a] != 0:
        return arr1[a]
    elif numbers[a] == -1:
        arr1[a] = 1
    else:
        arr1[a] = check(numbers[a], numbers, arr1) + 1
    return arr1[a]


def main():
    
    first_input = input()
    if first_input.__contains__('I'):
        second_input = int(input())
        third_input = list(map(int, input().strip().split()))
        aray(second_input, third_input)
    elif first_input.__contains__('F'):
        file_name = input()
        if file_name.__contains__('a'):
            print("INPUT-OUTPUT ERROR")
            return
        file = os.path.join(os.getcwd(), 'test', file_name)
        with open(file) as f:
            second_input = int(f.readline())
            third_input = list(map(int, f.readline().split()))
            aray(second_input, third_input)
    else:
        print("INPUT-OUTPUT ERROR")
        return
    print(int(c))


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
