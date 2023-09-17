
"""

#biraz daha zamhetli versiyonu sum liste içindekileri tekde toplar
for a in range(0, boy):
    boy_olcme[a] = int(boy_olcme[a]) 
    toplam += boy_olcme[a]
oran = int(round(toplam / boy, 0))
print(oran)


#for döngüleri
toplam = 0
boy_olcme = input("Belirli aralıklar giriniz: ").split()
boy = len(boy_olcme)
for a in range(0, boy):
    boy_olcme[a] = int(boy_olcme[a]) 
oran = int(round(sum(boy_olcme) / boy, 0))
print(oran)

#max min operatörlerini kullanmadan listedeki en buyuk ve en küçük sayıyı bulmak.
sayi = input("0 ile 100 arasındaki sayıları giriniz: ").split()
en_buyuk = int(sayi[0])
for a in range(0 ,len(sayi)):
    sayi[a] = int(sayi[a])
    if sayi[a] > en_buyuk:
       en_buyuk = sayi[a]
print(en_buyuk)

#fizz buss oyunu sayıların katları
for sayi in range(1, 101):
    if sayi % 3 == 0 and sayi % 5 == 0:
        print("FizzBuzz")
    elif sayi % 3 == 0:
        print("Fizz")
    elif sayi %  5 == 0:
        print("Buzz")
    else:
        print(f"{sayi}")
"""        
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
harf = int(input("Şifrenizde kaç tane harf istediğinizi yazınız: "))
sayi = int(input("Şifrenizde kaç tane sayı istediğinizi yazınız: "))
sembol = int(input("Şifrenizde kaç tane sayı istediğinizi yazınız: "))
sifre_liste = []
for h in range(1 , harf + 1):
    sifre_liste += random.choice(letters)
for s in range(1, sayi + 1):
    sifre_liste += random.choice(numbers)
for se in range(1, sembol + 1):  
    sifre_liste += random.choice(symbols) 
random.shuffle(sifre_liste)      
sifre = ""
for sayi1 in sifre_liste:          
    sifre += sayi1
print(f"Şifren: {sifre}")
    
