# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:41:31 2024

@author: nhat anh
"""
print("Kiểm tra tính hợp lệ của ngày tháng năm")
y = int(input("Nhập năm: "))
m = int(input("Nhập tháng: "))
if m < 1 or m > 12:
    print("Không hợp lệ")
else:
    d = int(input("Nhập ngày: "))
    if d < 1 or d > 31:
        print("Không hợp lệ")
    else:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            print("Năm là năm nhuận.")
            if m == 2:
                if d > 29:
                    print("Không hợp lệ")
                else:
                    print("Tháng này có 29 ngày.")
        else:
            print("Năm này không là năm nhuận.")
            if m == 2:
                if d > 28:
                    print("Không hợp lệ")
                else:
                    print("Tháng này có 28 ngày.")
            elif m == 4 or m == 6 or m == 9 or m == 11:
                if d > 30:
                    print("Không hợp lệ")
                else:
                    print("Tháng này có 30 ngày.")
            elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                if d > 31:
                    print("Không hợp lệ")
                else:
                    print("Tháng này có 31 ngày.")
            else:
                print("Không hợp lệ")