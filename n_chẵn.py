# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:55:26 2024

@author: ADMIN
"""

def get_positive_even_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0 and num % 2 == 0:
                return num
            else:
                print("Số nhập vào phải là số chẵn và lớn hơn 0. Vui lòng nhập lại.")
        except ValueError:
            print("Đầu vào không phải là số nguyên. Vui lòng nhập lại.")

def calculate_sum_of_even_numbers(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

n = get_positive_even_integer("Nhập số chẵn và lớn hơn 0 n: ")

result = calculate_sum_of_even_numbers(n)

print(f"Tổng S = 2 + 4 + 6 + ... + {n} là: {result}")
