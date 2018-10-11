#!/usr/bin/python
# -*- coding:utf-8 -*-
leng = 5
ticket = input("请问是否有票？有/没有")
if ticket == "有":
    print("欢迎进站安检！")
    length = int(input("请问你这把刀子的长度"))
    if length >= leng:
        print("携带管制物品，接受检查")
    else:
        print("请上车")
else:
    print("请先去买票")
