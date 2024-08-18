# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:08:25 2024

@author: nhat anh
"""
nguoichoi=float(input("Người chọn (1 la KEO,2 la BUA, la BAO): "))
from random import randint
mc=randint(1,3)
if mc==1:
    print("Máy chọn KEO")
elif mc==2:
    print("Máy chọn BUA")
elif mc==3:
    print("Máy chọn BAO")
if mc==nguoichoi:
    print("Kết quả HOA")
elif mc==1 and nguoichoi==2:
    print("WIN")
elif mc==1 and nguoichoi==3:
    print("LOSE")
elif mc==2 and nguoichoi==1:
    print("LOSE")
elif mc==2 and nguoichoi==3:
    print("WIN")
elif mc==3 and nguoichoi==1:
    print("WIN")
elif mc==3 and nguoichoi==2:
    print("LOSE")
else:
    print("Không hợp quy tắc trò chơi")