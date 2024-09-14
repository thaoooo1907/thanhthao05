# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:09:24 2024

@author: HP
"""
def tinh_tong(n):
  tong = 0
  for i in range(1, n+1):
    tong += 1 / i
  return tong
n = int(input("Nhập số lượng số hạng n: "))
ket_qua = tinh_tong(n)
print("Tổng của dãy số là:", ket_qua)

