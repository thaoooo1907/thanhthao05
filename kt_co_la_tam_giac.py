# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:26:20 2024

@author: ADMIN
"""

def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("Số nhập vào không phải là số nguyên dương. Vui lòng nhập lại.")
        except ValueError:
            print("Đầu vào không phải là số nguyên. Vui lòng nhập lại.")

def check_triangle_type(a, b, c):
    
    sides = sorted([a, b, c])
    a, b, c = sides

   
    if a + b > c:
        
        if a == b == c:
            return "Tam giác đều"
        elif a == b or b == c:
            
            if a**2 + b**2 == c**2:
                return "Tam giác vuông cân"
            else:
                return "Tam giác cân"
        else:
           
            if a**2 + b**2 == c**2:
                return "Tam giác vuông"
            else:
                return "Tam giác thường"
    else:
        return "Ba số không thể tạo thành tam giác"


a = get_positive_integer("Nhập cạnh a: ")
b = get_positive_integer("Nhập cạnh b: ")
c = get_positive_integer("Nhập cạnh c: ")


result = check_triangle_type(a, b, c)
print(f"Kết quả: {result}")
