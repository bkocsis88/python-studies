import random
szavak=[]
with open("magyar-szavak.txt","r",encoding="utf-8") as fajl_be:
    szavak=fajl_be.readlines()

print("Akasztófa játék".upper())
print("################"+"\n")
jatszunke=False
while (True):
    jatek=input("Van kedve egy akasztófa játékhoz? (i/n) ").lower()
    print()
    if (jatek == "i" or jatek == "igen"):
        jatszunke=True
    elif (jatek == "n" or jatek == "nem"):
        jatszunke=False
        break
    else:
        print("Kérem, igennel vagy nemmel feleljen!")
    
    if (jatszunke == True):
        feladvany=szavak[random.randint(0,len(szavak)-1)].rstrip('\n')
        megfejtes=list("_"*len(feladvany))
        rontasok_szama=10
        tippek_szama=0
        print(f"Nagyszerű! A szó {len(feladvany)} darab betűből áll, és {rontasok_szama} darab találatot adhat meg.\n")
        print(' '.join(megfejtes)+"\n")
        rossz_tippek=list()     
        jo_tippek=list()            
        while (True):
            if (feladvany == ''.join(megfejtes)):
                print("Gratulálok! Megoldotta!")
                break
            if (rontasok_szama == 0):
                print(f"Sajnálom, ez most nem sikerült. A feladvány {feladvany} szó volt.")
                break
            tipp=input("Kérem, adja meg a tippjét: ").lower()
            print()
            if (len(tipp) != 1):    
                print("Kérem, egy betűt adjon meg!\n")
                continue
            if (tipp == " "):
                print("Kérem, egy betűt adjon meg!\n")
                continue
            talalt=False
            index=0 
            for b in feladvany:
                if (b.lower() == tipp):
                    talalt=True
                    megfejtes[index]=b
                index+=1           
            if (talalt):           
                tippelt=False
                for x in jo_tippek:
                    if (x.lower() == tipp):
                        tippelt=True
                if (tippelt):
                    print("Ezt a betűt egyszer már tippelte.\n") 
                else:
                    jo_tippek.append(tipp)
                    tippek_szama+=1
                    print("Ez a tipp talált.")
            else:
                tippelt=False
                for b in rossz_tippek:
                    if (b.lower() == tipp):
                        tippelt = True
                if (tippelt):
                    print("Ez a betű már korábban sem volt jó.\n")
                else:
                    rontasok_szama-=1
                    tippek_szama+=1
                    rossz_tippek.append(tipp)
                    print("Ez a tipp nem talált.\n")
            print(' '.join(megfejtes)+"\n")
            print(f"Rossz tippek: {', '.join(rossz_tippek)}")
            print(f"Még {rontasok_szama} lehetősége van találgatni.")
            print(f"Eddig {tippek_szama} tippet tett meg.\n")
print("Sajnálom, talán majd máskor.")