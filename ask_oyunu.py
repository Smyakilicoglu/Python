# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 18:37:41 2023

"""
#aşk yüzde hesaplama oyunu
#isimleri birleştirip sonra küçültsen daha kolay olur.
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
isim_kucultme1 = name1.lower()
isim_kucultme2 = name2.lower()
t = int(isim_kucultme1.count("t") + isim_kucultme2.count("t"))
r = int(isim_kucultme1.count("r") + isim_kucultme2.count("r"))
u = int(isim_kucultme1.count("u") + isim_kucultme2.count("u"))
e = int(isim_kucultme1.count("e") + isim_kucultme2.count("e"))
sayi = t+r+u+e
l = int(isim_kucultme1.count("l") + isim_kucultme2.count("l"))
o = int(isim_kucultme1.count("o") + isim_kucultme2.count("o"))
v = int(isim_kucultme1.count("v") + isim_kucultme2.count("v"))
sayi1 = l+o+v+e
toplam = str(sayi) + str(sayi1)
toplama = int(toplam) #toplam = int(str(sayi) + str(sayi1)) aynı işlevi görüyor.
if toplama < 10 or toplama > 90:
    print(f"Your score is {toplam}, you go together like coke and mentos.")
elif toplama >= 40 and toplama <= 50:
    print(f"Your score is {toplam}, you are alright together.")
else:
    print(f"Your score is {toplam}.")
