# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:12:28 2024

@author: nhat anh
"""

a = float(input("Nhap canh a:"))
b = float(input("Nhap canh b:"))
c = float(input("Nhap canh c:"))
if  (a+b>c) and (a+c>b) and (c+b>a):
    print("a,b,c la ba canh cua tam giac")
else:
    print("a,b,c khoong phai la ba canh cua tam giac")