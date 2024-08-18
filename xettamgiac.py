# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:20:05 2024

@author: nhat anh
"""

a = float(input("Nhap canh a:"))
b = float(input("Nhap canh b:"))
c = float(input("Nhap canh c:"))
if  (a+b>c) and (a+c>b) and (c+b>a):
    if a==b==c:
        print("a,b,c la ba canh cua tam giac deu")
    elif a==b or a==c or b==c:
        print("a,b,c la ba canh cua tam can")
    elif (a*a==b*b+c*c) or (b*b==a*a+c*c) or (c*c==a*a+b*b):
        print("a,b,c la ba canh cua tam giac vuong ")
    else:
        print("a,b,c la ba canh cua tam giac thuong")
else:
    print("a,b,c khong phai la ba canh cua tam giac")