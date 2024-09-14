# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:06:05 2024

@author: HP
"""
def tinh_tong(x, n):
  tong = 0
  mau = 0
  for i in range(1, n+1):
    mau += i
    tong += x**i / mau
  return tong
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập số lượng số hạng n: "))
ket_qua = tinh_tong(x, n)
print("Tổng của dãy số là:", ket_qua)