# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 02:09:14 2021

@author: hbbdm
"""

menu = {"라면":4000,
        "비빔밥":5000,
        "국수":6000,
        "고등어":8000,
        "음료":2000,
        "밥":1000,
        "피자":3500,
        "김밥":2500,}
print("3ta taom buyurtma bering.")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1} - taom:").lower())
    
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} won")
    else:
        print(f"죄송합니다, {buyurtma} 없습니다~~")