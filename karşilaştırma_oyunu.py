# -*- coding: utf-8 -*-
"""

"""
import random
from oyun_kişileri import data

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
print(logo)

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

"""
sözlükteki kişilerden ikisini seçip takipçi sayılarını karşılaştır doğru bilirsen seçtiğin
kişiyle başka random birinin takipçisini karşılaştır kaybedersen kaç tane bildiğini gösteri oyundan çıksın.
"""
kac_tahmin = 0
secim1 = random.randint(0, len(data) - 1)
secilenler1 = data[secim1]
secim2 = random.randint(0, len(data) - 1)
secilenler2 = data[secim2]

def random_1(a):
    isim = secilenler1['name']
    tanim = secilenler1['description']
    ulke = secilenler1['country']
    print(f"Seçenek A : {isim}, bir {tanim}, {ulke}'den.")
def random_2(b):
    isim = secilenler2['name']
    tanim = secilenler2['description']
    ulke = secilenler2['country']
    print(f"Seçenek B : {isim}, bir {tanim}, {ulke}'den.")
cikma = True
random_1(secilenler1)
print(vs)
random_2(secilenler2)
   

while cikma:
    sec = input("Sence hangisinin daha çok takipçisi vardır? Seç: ").lower()
    sayi1 = int(secilenler1['follower_count'])
    sayi2 = int(secilenler2['follower_count'])
    if sec == 'a':
        if sayi1 > sayi2:
            print("Seçtiğiniz kişi daha fazla takipçiye sahip. Doğru\n")
            random_1(secilenler1)
            secim3 = random.randint(0, len(data) - 1)
            print(vs)
            secilenler3 = data[secim3]
            random_2(secilenler3)
            kac_tahmin += 1
        else:
            print(f"Kaybettin! {kac_tahmin} kere doğru bildin.")
            cikma = False
    if sec == 'b':
        if sayi1 > sayi2:
            print("Seçtiğiniz kişi daha fazla takipçiye sahip. Doğru\n")
            random_1(secilenler2)
            secim3 = random.randint(0, len(data) - 1)
            print(vs)
            secilenler3 = data[secim3]
            random_2(secilenler3)
            kac_tahmin += 1
        else:
            print(f"Kaybettin! {kac_tahmin} kere doğru bildin.")
            cikma = False
    

