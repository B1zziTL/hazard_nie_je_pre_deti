#vlozenie modulov
import random

#zadeklarovanie premennych a zoznamov
jeden = 0
dva = 0
tri = 0
styri = 0
pat = 0
sest = 0
zadane_cisla = []
importovane_cisla = []
vyzrebovane = []

#otvorenie suboru
subor = open("loteria_2.txt","r")

for i in range(6): #cyklus na zadanie cisel loterie
    zrebujeme = random.randint(1,49)
    vyzrebovane.append(zrebujeme)

for riadok in subor: #cyklus na zistenie poctu spravnych tipov
    riadocek = riadok.split()
    for cislo in riadocek:
        importovane_cisla.append(int(cislo))

    #zistenie spravnych cisel
    prienik = set(importovane_cisla).intersection(vyzrebovane)

    #podmienky na spocitanie spravnych tipov
    if len(prienik) == 1:
        jeden += 1
    elif len(prienik) == 2:
        dva += 1
    elif len(prienik) == 3:
        tri += 1
    elif len(prienik) == 4:
        styri += 1
    elif len(prienik) == 5:
        pat += 1
    elif len(prienik) == 6:
        sest += 1

#spracovanie inputu
tvoje_cisla = input("Zadaj šesť čísel:")
daco = tvoje_cisla.split()

for ii in daco: #cyklus na vlozenie cisel do zoznamu
    zadane_cisla.append(int(ii))

#zistenie spravnych cisel
rovnake = set(zadane_cisla).intersection(vyzrebovane)

#podmienky na vypisanie info
if len(rovnake) != 0:
    print("Správne si tipol tieto čísla:",*rovnake)
    print("Dokopy správne máš:",len(rovnake),"\n")
else:
    print("Netipol si ani jedno správne číslo","\n")

#vypisanie info jednotlivych poctov
print("Jedno správne:",jeden,"krát")
print("Dve správne:",dva,"krát")
print("Tri správne:",tri,"krát")
print("Štyri správne:",styri,"krát")
print("Päť správne:",pat,"krát")
print("Šesť správne:",sest,"krát")

#uzavretie suboru
subor.close()
