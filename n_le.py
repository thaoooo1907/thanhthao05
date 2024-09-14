# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:56:21 2024

@author: ADMIN
"""

def get_positive_odd_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0 and num % 2 != 0:
                return num
            else:
                print("Số nhập vào phải là số lẻ và lớn hơn 0. Vui lòng nhập lại.")
        except ValueError:
            print("Đầu vào không phải là số nguyên. Vui lòng nhập lại.")

def calculate_product_of_numbers(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

n = get_positive_odd_integer("Nhập số lẻ và lớn hơn 0 n: ")

result = calculate_product_of_numbers(n)

print(f"Tích S = 1 × 2 × 3 × ... × {n} là: {result}")
