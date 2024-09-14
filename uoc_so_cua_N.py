# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:42:18 2024

@author: Student
"""


def is_positive_integer(value):
    return value.isdigit() and int(value) > 0


while True:
    N = input("Nhập một số nguyên dương: ")
    if is_positive_integer(N):
        N = int(N)
        break
    else:
        print("Số nhập vào không hợp lệ. Vui lòng nhập lại.")


print(f"Các ước số của {N} là:", end=" ")
for i in range(1, N + 1):
    if N % i == 0:
        print(i, end=" ")
print()

