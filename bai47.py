# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:34:24 2024

@author: Admin
"""
def tim_bo_nghiem_lon_nhat(target):
  max_sum = 0
  for x in range(target//2, 0, -1):
    for y in range((target - 2*x)//7, 0, -1):
      z = (target - 2*x - 7*y) // 9
      if z > 0 and 2*x + 7*y + 9*z == target:
        current_sum = x + y + z
        if current_sum > max_sum:
          max_sum = current_sum
          print(f"Bộ nghiệm: ({x}, {y}, {z})")
