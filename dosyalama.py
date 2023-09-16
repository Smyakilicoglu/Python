# -*- coding: utf-8 -*-
"""
Created on Fri May 19 21:32:00 2023

@author: Sümeyra KILIÇOĞLU
"""
#1) Dosya içe yazı yazdırma=
from pathlib import Path
p = Path("spam.txt")
p.write_text("Merhaba gençlik naber?")
#dosyanın içindeki sayıyı ekrana yazdırmayı sağlama.
p.read_text()
"""
#dosyayı açma=
1) helloFile = open(C:\\Users\\Sümeyra KILIÇOĞLU\\spam.txt)
2) helloFile = open(Path.home() / 'spam.txt')
#dosyadaki yazıyı koda yazdırma=
helloContent = helloFile.read()
helloContent
uzun metinler için dosya yazdırmada=
helloContent = helloFile.readlines()
helloContent
close() #dosyayı kapatmaya yarar.

######dosya aç yazdır######
beconFile = open('hello.txt', 'w')  
beconFile.write('merhaba insanlar nasılsınız?\n')
beconFile.close()
beconFile = open('hello.txt', 'a')
beconFile.write('dünden daha fakirsiniz...') 

################## shelve modülü ##############
#bir takım dataları liste mantığıyla dosyalama 
#ÇOK KULLANILMAZ HOCA SORMAZ!!!!!!!!!!!!!!!!!!!!!!!!!!!
import shelve 
shelfFile = shelve.open("mydata")
cats = ["karam", "yumurta", "arı"]
shelfFile["cats"] = cats
shelfFile.close()

##### SHUTİL MODÜLÜ #### SINAVDA SORULMAZ
kopyala, yapıştır, dosyayı sil vs işlemleri bu modülle yapılır.
impoert shutil,os
from pathlib import Path
p = Path.home()
shutil.copy(p / 'spam.txt' , p / 'some_folder/spam2.txt') 
#dosyadan dosyaya kopyala spam2 adını ver.
Klasör taşı ve değiştir. move
####### OS ######
işletim sistemleriyle ilgili şeyler bu kütüphanede bulunur.
"""
 
