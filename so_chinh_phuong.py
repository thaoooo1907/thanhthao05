# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:42:45 2024

@author: ADMIN
"""

import math

def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("Số nhập vào phải là số nguyên dương. Vui lòng nhập lại.")
        except ValueError:
            print("Đầu vào không phải là số nguyên. Vui lòng nhập lại.")

def is_perfect_square(n):
   
    root = int(math.sqrt(n))
   
    return root * root == n


n = get_positive_integer("Nhập số nguyên dương n: ")


if is_perfect_square(n):
    print(f"{n} là số chính phương.")
else:
    print(f"{n} không phải là số chính phương.")
