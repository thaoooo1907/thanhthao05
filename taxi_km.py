# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:32:00 2024

@author: ADMIN
"""

def get_positive_float(prompt):
    while True:
        try:
            km = float(input(prompt))
            if km > 0:
                return km
            else:
                print("Số km phải là số dương. Vui lòng nhập lại.")
        except ValueError:
            print("Đầu vào không phải là số hợp lệ. Vui lòng nhập lại.")

def calculate_taxi_fare(km):
    first_km_price = 15000
    second_to_fifth_km_price = 13500
    beyond_sixth_km_price = 11000
    discount_threshold = 120
    discount_rate = 0.10
    
    if km <= 1:
        fare = km * first_km_price
    elif km <= 5:
        fare = first_km_price + (km - 1) * second_to_fifth_km_price
    else:
        fare = first_km_price + 4 * second_to_fifth_km_price + (km - 5) * beyond_sixth_km_price
    
    if km > discount_threshold:
        fare -= fare * discount_rate
    
    return fare

km = get_positive_float("Nhập số km đi được: ")


total_fare = calculate_taxi_fare(km)

print(f"Tổng tiền cước taxi cho {km} km là: {total_fare:.0f} đ")
