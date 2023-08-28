# -*- coding: utf-8 -*-
"""
Created on Fri May  5 17:14:11 2023

@author: Sümeyra KILIÇOĞLU

import math
math.ceil(#girilen ondalıklı sayıyı tama çevirir. yuvarlar)
          
#sezar şifreleme:
alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
mesaj = input("Type your message:\n").lower()
sayi = int(input("Type the shift number:\n"))
def kaydirma(a, b): 
    sezar_sifre = ""
    for harf in a:
        pozisyon = alfabe.index(harf)
        yeni_pozisyon = pozisyon + b
        yeni_harf = alfabe[yeni_pozisyon]
        sezar_sifre += yeni_harf
    print(f"Sezar şifrelemede bu yazının karşılığı: {sezar_sifre}")
def bulma(a, b):
    sezar_ters = ""
    for harf in a:
        pozisyon = alfabe.index(harf)
        yeni_pozisyon = pozisyon - b
        yeni_harf = alfabe[yeni_pozisyon]
        sezar_ters += yeni_harf
    print(f"Sezar şifrelemenin normalde karşılığı: {sezar_ters}")
if direction == "encode":
    kaydirma(mesaj, sayi)
else:
    bulma(mesaj, sayi)

from art import logo
print(logo)
"""
alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def kullanilan_fonksiyonlar(a, b):
    sezar_sifre = ""
    for harf in a:
        if harf in alfabe:
            pozisyon = alfabe.index(harf)
            if direction == 'encode':
                yeni_pozisyon = pozisyon + b
            else:
                yeni_pozisyon = pozisyon - b
            yeni_harf = alfabe[yeni_pozisyon]
            sezar_sifre += yeni_harf
        else:
            sezar_sifre += harf
    if direction == 'encode':
        print(f"Sezar şifrelemede bu yazının karşılığı: {sezar_sifre}")
    else:
        print(f"Sezar şifrelemenin normalde karşılığı: {sezar_sifre}")      
sayi = False
while not sayi:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    mesaj = input("Type your message:\n").lower()
    sayi = int(input("Type the shift number:\n"))
    sayi = sayi % 26
    kullanilan_fonksiyonlar(mesaj,sayi)
    cikma = input("Eğer şifrelemede çıkmak istiyorsanız 'evet' yazın eğer çıkmak istiyorsanız 'hayır' yazınız: ")
    if cikma == "evet":
        sayi = True
        print("Goodbye!")
        





