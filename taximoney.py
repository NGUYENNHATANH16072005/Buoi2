# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:38:45 2024

@author: nhat anh
"""
a = float(input("So km quang duong taxi di duoc:"))
if a<=1:
    st=20
    print("so tien la", st)
elif a<=3:
    st=a*13
    print("so tien la", st)
elif 4<=a<=8:
    st=3*13+(a-3)*12
    print("so tien", st)
elif 8<a:
    st=3*13+(a-3)*12+a*10
    print("so tien", st)
if st > 100:
    stc=st*0.92
    print("so tien cuoi", stc)
