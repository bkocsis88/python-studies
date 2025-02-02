import random, math
print("Számkitalálós játék.")
print()
print("A játékot két féleképpen lehet játszani. Ön is gondolhat egy számra, akkor a program találgat. Vagy a program gondol egy számra és Ön találgathat. Válasszon, és játszon!")
print()
nyert=0
vesztett=0
def Felhasznalotalalki():
    global nyert
    global vesztett
    print("Most Ön találja ki a számot!")
    szam=random.randint(0,10)
    limit=10
    tippek_szama=0
    tipp=-1
    kerdes="Kérem, adjon meg egy számot 0 és 100 között: "
    while (tipp != szam):
        if limit==tippek_szama:
            break 
        tipp=int(input(kerdes))
        tippek_szama+=1
        if tipp > szam:
            print("A tippje nagyobb, mint a gondolt szám.")
        else:
            print("A tippje kisebb, mint a gondolt szám.")
        kerdes="Sajnos nem jó számot adott meg, adjon meg egy újabb tippet 0 és 100 között: "
    if tipp==szam:
        nyert+=1
        print("Gratulálunk, eltalálta a számot!")
    else:
        vesztett+=1
        print("Sajnálom, Ön vesztett!")
def Kerdes (szoveg):
    valami=""
    while True:
        valami=input(szoveg+ "(i/n) :")
        if valami == "i" or valami == "n":
            break
        else:
            print("Helyes válaszok: i/n")
            continue
    return valami      
def Kozep(min,max):
    szam=math.floor((min+max)/2)
    return szam
def Programtalalki():
    global nyert
    global vesztett
    print("Most a program találja ki a számot! Gondoljon egy számra!")
    limit=10
    min=0
    max=100
    tipp=random.randint(min,max)
    for _ in range(limit):
        print(f"A tippem: {tipp}. ")
        helyes_e=""
        while True:
            helyes_e=input("Ez a tipp helyes? (i=helyes, < = a szám kisebb, > = a szám nagyobb): ")
            if helyes_e =="i":
                print("Sajnálom, a gép nyert!")
                vesztett+=1
                break
            elif helyes_e == ">":
                min=tipp
                break
            elif helyes_e == "<":
                max=tipp
                break
            else:
                print("Sajnos nem jó karaktereket adott meg. (i=helyes, < = a szám kisebb, > = a szám nagyobb).")   
                continue
        if helyes_e == ">" or helyes_e == "<":
            tipp=Kozep(min,max)
        else:
            break
    if helyes_e != "i":
        print("Gratulálunk, Ön nyert!")
        nyert+=1
jatek_mod=input("Szeretne gondolni egy számra? (i/n) ")
while (True):
    if jatek_mod == "i":
        Programtalalki()
        tovabbi_jatek=Kerdes("Szeretne még játszani?")
        if (tovabbi_jatek == "i"):
            continue
        elif (tovabbi_jatek == "n"):
            break    
    elif jatek_mod == "n":
        Felhasznalotalalki()
        tovabbi_jatek = Kerdes("Szeretne még játszani?")
        if (tovabbi_jatek == "i"):
            continue
        elif (tovabbi_jatek == "n"):
            break
    else:
        print("Nem sikerült választani. Lehetséges válaszok i/n.")
print(f"A játéknak vége! Körök száma: {nyert+vesztett}. Megnyert körök száma: {nyert}. Vesztett körök száma: {vesztett}.")

    