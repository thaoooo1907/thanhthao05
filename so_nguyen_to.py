# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:46:11 2024

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

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  
    if n % 2 == 0:
        return False 
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


n = get_positive_integer("Nhập số nguyên dương n: ")

if is_prime(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
