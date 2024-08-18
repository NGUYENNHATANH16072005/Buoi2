# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 12:51:06 2024

@author: nhat anh
"""
distance = float(input("Nhap diem trung binh GPA:"))
if distance < 3.5:
    print("Hoc luc Kem")
elif 3.5 <= distance < 5.0 :
    print("Hoc luc Yeu")
elif 5.0 <= distance < 7.0:
    print("Hoc luc Trung binh")
elif 7.0 <= distance < 8.0:
    print("Hoc luc Kha")
elif 8.0 <= distance < 9.0:
    print("Hoc luc Gioi")
elif 9.0 <= distance <= 10:
    print("Hoc luc Xuat sac")