#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return 

    list = [0, 1]

    while len(list) < length:
        next_number = list[-1] + list[-2]
        list.append(next_number)

    print(list[:length])
pass