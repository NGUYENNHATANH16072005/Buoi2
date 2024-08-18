# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:29:37 2024

@author: nhat anh
"""
import math
a = float(input("Nhap he so a:"))
b = float(input("Nhap he so b:"))
c = float(input("Nhap he so c:"))
delta = b*b - 4*a*c
if delta < 0:
   print("Phuong trinh Vo nghiem")
elif delta == 0:
   print("Phuong trinh co Nghiem kep x1=x2=",-b/2*a)
else:
    print("Phuong trinh co hai Nghiem phan biet")
    print("x1=",((-b) + math.sqrt(delta))/(2*a))
    print("x2=",((-b) - math.sqrt(delta))/(2*a))
    
   
