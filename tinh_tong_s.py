# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:52:02 2024

@author: ADMIN
"""

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

def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


n = get_positive_integer("Nhập số nguyên dương n: ")


result = calculate_sum(n)


print(f"Tổng S = 1 + 2 + 3 + ... + {n} là: {result}")
