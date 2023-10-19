# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:42:33 2023

"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#Kahve makinesi:

logo = """██   ██  █████  ██   ██ ██    ██ ███████     ███    ███  █████  ██   ██ ██ ███    ██ ███████ ███████ ██ 
██  ██  ██   ██ ██   ██ ██    ██ ██          ████  ████ ██   ██ ██  ██  ██ ████   ██ ██      ██      ██ 
█████   ███████ ███████ ██    ██ █████       ██ ████ ██ ███████ █████   ██ ██ ██  ██ █████   ███████ ██ 
██  ██  ██   ██ ██   ██  ██  ██  ██          ██  ██  ██ ██   ██ ██  ██  ██ ██  ██ ██ ██           ██ ██ 
██   ██ ██   ██ ██   ██   ████   ███████     ██      ██ ██   ██ ██   ██ ██ ██   ████ ███████ ███████ ██ """
print(logo)
                                                                                                        
money = 0
penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

def miktar():
    for _ in resources:
        print(f"{_} = {resources[_]}")
    print(f"Money = ${money}")

def malzeme_mik():
    print(f"Water = {kalan_su}ml")
    print(f"Milk = {kalan_sut}ml")
    print(f"Coffee = {kalan_kahve}g")
    print(f"Money = ${money}")


def para_mik(x):
    global money
    print("Kahveni almak için para at.")
    pen = int(input("Kaç penny vereceksin? "))
    nic = int(input("Kaç nickel vereceksin? "))
    dim = int(input("Kaç dime vereceksin? "))
    quar = int(input("Kaç quarter vereceksin? "))
    miktar = (pen*penny)+(nickel*nic)+(dime*dim)+(quarter*quar)   
    if MENU[x]["cost"] == miktar:
        print("Kahve hazır!")
        money = round(money + miktar, 2)
    elif MENU[x]["cost"] > miktar:
        print("Bu para miktarı yeterli değil!")
    elif MENU[x]["cost"] < miktar:
        para_ustu = round(miktar - MENU[f"{x}"]["cost"], 2)
        print(f"Lütfen para üstünüzü alınız {para_ustu}. Kahveniz hazır!")
        money = round(money + (miktar - para_ustu), 2)

secim = ""      
def secim_():
    global secim
    secim = input("İçmek istediğiniz kahveyi seçiniz(Espresso/Latte/Cappuccino): ").lower()

secim_()
if secim == 'report':
    miktar()

secim_()
if secim == 'report':
    malzeme_mik()
elif secim == 'espresso' or secim == 'latte' or secim == 'cappuccino':
    para_mik(secim)
    kalan_su = resources["water"]  - MENU[secim]["ingredients"]["water"]
    kalan_sut = resources["milk"]  - MENU[secim]["ingredients"]["milk"]
    kalan_kahve = resources["coffee"]  - MENU[secim]["ingredients"]["coffee"]     

while True:
    secim_()
    if secim == 'report':
        malzeme_mik()
    elif secim == 'espresso' or secim == 'latte' or secim == 'cappuccino':
        if MENU[secim]["ingredients"]["water"] > kalan_su:
            print("Bu kahveyi yapmak için yeterli su yok.")
            continue
        elif MENU[secim]["ingredients"]["milk"] > kalan_sut:
            print("Bu kahveyi yapmak için yeterli süt yok.")
            continue
        elif MENU[secim]["ingredients"]["coffee"] > kalan_kahve:
            print("Bu kahveyi yapmak için yeterli kahve yok.")
            continue
        para_mik(secim)
        kalan_su -= MENU[secim]["ingredients"]["water"]
        kalan_sut -= MENU[secim]["ingredients"]["milk"]
        kalan_kahve -= MENU[secim]["ingredients"]["coffee"]
