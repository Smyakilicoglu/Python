# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:58:31 2023

@author: Sümeyra KILIÇOĞLU

2 İkili.  
3 Üçlü.  
4 Dörtlü.
5 Beşli.
6 Altılı.
7 Yedili.
8 Sekizli.
9 Dokuzlu.
10 Onlu.
"""
# BlackJack oyunu
import random
toplam_kartlar = ["papaz", "vale", "kız", "joker",2,3,4,5,6,7,8,9,10]
onlar = toplam_kartlar[0:4]
for a in onlar:
    a = 10

random_sayi = random.randint(0, len(toplam_kartlar) - 1)
a = toplam_kartlar[random_sayi]
random_sayi1 = random.randint(0, len(toplam_kartlar) -1)
b = toplam_kartlar[random_sayi1]
print(f"Kartların: {a}, {b}")

if a == 'vale' or a == 'papaz' or a == 'kız' or a == 'joker':
    if b == 'vale' or b == 'papaz' or b == 'kız' or b == 'joker':
        sayi = 20
        print(f"Mevcut puan: {sayi}")
    else:
        sayi = 10+b
        print(f"Mevcut puan: {sayi}")
else:
    if b == 'vale' or b == 'papaz' or b == 'kız' or b == 'joker':
        sayi = 10+a
        print(f"Mevcut puan: {sayi}")
    else:
        sayi = a+b
        print(f"Mevcut puan: {sayi}")

bs_random_sayi = random.randint(0, len(toplam_kartlar) - 1)
bs_a = toplam_kartlar[bs_random_sayi]
print(f"Bilgisayarın ilk kartı: {bs_a}")
cikma = True
while cikma:
    secim = input("Bir kart daha çekmek istiyorsan 'Evet' yaz. Çekmek istemiyorsan 'Hayır' yaz: ").title()
    if secim == 'Evet':
        c = toplam_kartlar[random.randint(0, len(toplam_kartlar) - 1)]
        print(f"En son aldığın kart: {c}")
        if c == 'vale' or c == 'papaz' or c == 'kız' or c == 'joker':
            sayi = sayi + 10
            print(f"Son eldeki kartlarınızın toplamı: {sayi}")
        else:
            sayi = sayi + c
            print(f"Son eldeki kartlarınızın toplamı: {sayi}")
    else:
        cikma = False
        bs_random_sayi1 = random.randint(0, len(toplam_kartlar) - 1)
        bs_b = toplam_kartlar[bs_random_sayi1]
        print(f"Bilgisayarın ikinci kartı: {bs_b}")
        if bs_a == 'vale' or bs_a == 'papaz' or bs_a == 'kız' or bs_a == 'joker':
            if bs_b == 'vale' or bs_b == 'papaz' or bs_b == 'kız' or bs_b == 'joker':
                sayi1 = 20
                print(f"Bilgisayarın mevcut puanı: {sayi1}")
            else:
                sayi1 = 10 + bs_b
                print(f"Bilgisayarın mevcut puanı: {sayi1}")
        else:
            if bs_b == 'vale' or bs_b == 'papaz' or bs_b == 'kız' or bs_b == 'joker':
                sayi1 = 10 + bs_a
                print(f"Bilgisayarın mevcut puanı: {sayi1}")
            else:
                sayi1 = bs_a + bs_b
                print(f"bilgisayarın mevcut puanı: {sayi1}")

if sayi > 21 or sayi1 > 21:
    print("Kaybettin! Kartlarının toplamı 21'den büyük bir değer çıktı.")
elif sayi1 > sayi:
    print(f"Kaybettin! Benim kartlarımın toplamı ({sayi}) senin kartlarının toplamından ({sayi1}) fazla.")
elif sayi > sayi1:
    print(f"Kazandın! Senin kartlarının toplamı ({sayi}) benim kartlarımın toplamından ({sayi1}) fazla.")
elif sayi == sayi1:
    print("Berabere...")
    