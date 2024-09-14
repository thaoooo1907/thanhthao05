# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:59:30 2024

@author: Student
"""

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

while True:
    try:
        month = int(input("Nhập tháng (1-12): "))
        year = int(input("Nhập năm: "))
        if 1 <= month <= 12 and year > 0:
            break
        else:
            print("Tháng phải trong khoảng 1-12 và năm phải là số nguyên dương. Vui lòng nhập lại.")
    except ValueError:
        print("Vui lòng nhập số nguyên.")

days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(f"Số ngày trong tháng {month} năm {year} là: {days_in_month[month - 1]}")