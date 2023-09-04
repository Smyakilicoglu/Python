# -*- coding: utf-8 -*-
"""
Created on Fri May  5 17:42:18 2023

"""

#asal sayı kodlaması
sayi = int(input("Bir sayı giriniz: "))
def asal_sayi_(n):
    for a in range(2, n-1):
        a += 1
        if n % a != 0:
            return "asal sayıdır."
        else:
            return "Sayı asal sayı değildir."
asal_sayi_(sayi)


