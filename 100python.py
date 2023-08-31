# -*- coding: utf-8 -*-
"""
"""

print("Welcome to the tip calculator")
many = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
pay = str((percentage + many) / people)
print("Each person should pay: $" + pay[0:2])

#aynı kodun farklı versiyonu
print("Welcome to the tip calculator")
many = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
yuzde = percentage / 100
pay = round((yuzde + many) / people , 2)
print(f"Each person should pay: ${pay}")


#iki basamaklı sayı yazdırıp bu basamakları topla
sayi = input("İki basamaklı bir sayı yazınız: ")
sayi_bir = sayi[0]
sayi_iki = sayi[1]
toplam = int(sayi_bir) + int(sayi_iki)
print(toplam)

#round sayıyı yuvarlar.
print(round(10 / 3)) #virgülden sonraki ikinci basamagı yuvarla.


#SINAVDA SAKIN BU METODU KULLANMA!!!
#Bir yılda 365 gün, yılda 52 hafta ve yılda 12 ay vardır.

print("Merhaba şuanki yaşını ve öleceğini düşündüğün yaşı yaz ve ne kadar zamanın olduğunu gör.")
su_anki_yas = int(input("Lütfen şu anki yaşınızı giriniz: "))
yas = int(input("Öleceğinizi düşündüğünüz yaşı giriniz: "))
ay = (yas - su_anki_yas)*12
hafta = (yas - su_anki_yas)*52
gun = (yas - su_anki_yas)*365
print(f"Ölmenize {gun} gün, {hafta} hafta, {ay} ayınız kaldı.")


#boyları 120 cm den butuk olan kısılerın gondola binebilecek olması 

boy = int(input("Şu anki mevcut boyunuzu giriniz: "))
if boy >= 120:
    print("Gondola binebilirsiniz.")
else:
    print("Gondola binmek için boyunuz yeterli değildir.")

#kilo ölçer.
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
oran = int(round(weight / (height**2)))
if oran <= 18 :
    print(f"Your BMI is {oran}, you are underweight.")
elif oran <= 25:
    print(f"Your BMI is {oran}, you have a normal weight.")
elif oran <= 30:
    print(f"Your BMI is {oran}, you are slightly overweight.")
elif oran <= 35:
    print(f"Your BMI is {oran}, you are obese.")
else:
    print(f"Your BMI is {oran}, you are clinically obese.")

#iç içe if else örnegi.
print("Hızlı Tiren!")
yas = int(input("Hızlı tirene binebilmek için yaşınızı giriniz: "))
if yas >= 15:
    boy = int(input("Hızlı tirene binebilmek için bir de boyunuzu giriniz: "))
    if boy >= 120:
        print("Hızlı tirene binebilirsiniz.")
    else:
        print("Boyunuz yetmemektedir, hızlı tirene binemezsiniz.")
else:
    print("yaşınız yetmemektedir, hızlı tirene binemezsiniz.")
    
#artık yıl hesaplama
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not last year.")
    else:
        print("Last year.")
    print("Leap year.")
else:
    print("Not leap year.")


