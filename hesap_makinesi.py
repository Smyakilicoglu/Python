# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:36:49 2023

@author: Sümeyra KILIÇOĞLU

#Title baş harfleri büyük yapar diğerleri büyükse küçültür.
"""
print("Hesap makinesi uygulamasına hoş geldiniz.")

def hesap_mak():
    print("Toplama İşlemi (+)")
    print("Çıkarma İşlemi (-)")
    print("Çarpma İşlemi (*)")
    print("Bölme İşlemi (/)")
    
    secenek = input("Hangi hesabı seçtiğinizi yazınız: ")
    sayi1 = float(input("İşlem yapmak istediğiniz birinci sayıyı giriniz: "))
    sayi2 = float(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz: "))
        
    
    if secenek == '+':
        sec1 = sayi1 + sayi2
        print(f"{sayi1} + {sayi2} = {sec1}")
    elif secenek == '-':
        sec1 = sayi1 - sayi2
        print(f"{sayi1} - {sayi2} = {sec1}")
    elif secenek == '*':
        sec1 = sayi1 * sayi2
        print(f"{sayi1} * {sayi2} = {sec1}")
    elif secenek == '/':
        sec1 = sayi1 / sayi2
        print(f"{sayi1} / {sayi2} = {sec1}")
    
    
    cikma = False
    while not cikma:
        cıkma = input("Eğer hesap makinesinden devam etmek istiyorsanız 'Evet' istemiyorsanız 'Hayır' yazınız ve yeni hesap yapınız: ").title()
        if cıkma == 'Evet': 
            secenek = input("Hangi hesabı seçtiğinizi yazınız: ")
            sayi2 = float(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz: "))
            sayi1 = sec1
            while True:
                if secenek == '+':
                    sec1 = sayi1 + sayi2
                    print(f"{sayi1} + {sayi2} = {sec1}")
                elif secenek == '-':
                    sec1 = sayi1 - sayi2
                    print(f"{sayi1} - {sayi2} = {sec1}") 
                elif secenek == '*':
                    sec1 = sayi1 * sayi2
                    print(f"{sayi1} * {sayi2} = {sec1}")
                elif secenek == '/':
                    sec1 = sayi1 / sayi2
                    print(f"{sayi1} / {sayi2} = {sec1}")
                break       
        else:
            cikma = True
            hesap_mak()
hesap_mak()