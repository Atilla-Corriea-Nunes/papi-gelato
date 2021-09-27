def imsorry():
    print("Sorry, dat snap ik niet")

def hoorncalc():
    print("Horentje         "+ str(hoorncounter) +" x €1.25   = €"+ str(round(hoornkosten, 2)))

def bakjecalc():
    print("Bakje            "+ str(bakjecounter) +" x €0.75   = €"+ str(round(bakjekosten, 2)))

def toppings():
    if (toppingkosten > 0):
        print("Topping          1 x €"+ str(toppingkosten) +"    = €"+ str(toppingkosten))
    else:
        pass
def bonnetjeeinde():
    print("                              ------ +")



end = False
hoorncounter = 0
bakjecounter = 0
heeftbakjebesteld = False
heefthornbesteld = False
hoeveelheidoplsaan = 0
hoeveelheidbakje = 0
hoeveelheidhoorn = 0
toppingtimes = 0
toppingkosten = 0

print("Welkom bij Papi Gelato.")
print("")
while (end == False):
    hoeveelheid = ("")
    aantalvraag = ("")
    x = 1
    counter = 0

    while (True):
        hoeveelheid = input("Hoeveel bolletjes wilt u? ")
        if (int(hoeveelheid.isnumeric()) == False):
            imsorry()
            continue
        elif (int(hoeveelheid) > 8):
            print("Sorry, zulke grote bakken hebben we niet")
            continue
        elif (int(hoeveelheid) == 1 or int(hoeveelheid) == 2 or int(hoeveelheid) == 3):
            break
        elif (int(hoeveelheid) > 3 and int(hoeveelheid) < 9):
            print("Dan krijgt u van mij een bakje met "+ str(hoeveelheid) +" bolletjes")
            keuze = ("bakje")
            heeftbakjebesteld = True
            hoeveelheidbakje = int(hoeveelheidbakje) + 1
            bakjecounter = bakjecounter + 1
            break
        elif (int(hoeveelheid.isnumeric()) == True):
            imsorry()
            continue
    if (hoeveelheidoplsaan == 0):
        hoeveelheidoplsaan = 0 + int(hoeveelheid)
    else:
        hoeveelheidoplsaan = int(hoeveelheidoplsaan) + int(hoeveelheid)

    if (int(hoeveelheid) > 3 and int(hoeveelheid) < 9):
       print("")
    else:
         while (True):
            aantalvraag = input("Wilt u deze "+ str(hoeveelheid) +" bolletje(s) in A) een hoorntje of B) een bakje? (Hoorn/Bakje) ")
            if (aantalvraag.lower() == "hoorn" ):
             keuze = ("hoorn")
             heefthornbesteld = True
             hoeveelheidhoorn =  int(hoeveelheidhoorn) + 1
             hoorncounter = hoorncounter + 1
             break
            elif (aantalvraag.lower() == "bakje"):
             keuze = ("bakje")
             heeftbakjebesteld = True
             hoeveelheidbakje = int(hoeveelheidbakje) + 1
             bakjecounter = bakjecounter + 1
             break
            else:
             print("Sorry dat snap ik niet...")
             continue

    while (True):
        whattopping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
        if (whattopping.lower() == "b" or whattopping.lower() == "c" or whattopping.lower() == "d" or whattopping.lower() == "a"):
            break
        else:
            print("Sorry dat snap ik niet...")
            continue

    
    while (int(hoeveelheid) > int(counter)):
        bolsmaak = input("Welke smaak wilt u voor bolletje nummer "+ str(counter + 1) +"? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
        if  (int(hoeveelheid) < int(counter)):
            break

        elif (bolsmaak.lower() == "a" or bolsmaak.lower() == "c" or bolsmaak.lower() == "m" or bolsmaak.lower() == "v"):
            counter = int(counter) + 1
            continue
        elif (bolsmaak.lower() != "a" or bolsmaak.lower() != "c" or bolsmaak.lower() != "m" or bolsmaak.lower() !=  "v"):
            imsorry()
            continue
    
    if (whattopping.lower() == "b"):
        toppingkosten = float(toppingkosten) + 0.50
    elif (whattopping.lower() == "c"):
        toppingkosten = float(toppingkosten) + float(hoeveelheid) * 0.30
    elif (whattopping.lower() == "d"):
        toppingkosten = float(toppingkosten) + float(hoeveelheid) + (float(hoeveelheidbakje) * 0.90 + float(hoeveelheidhoorn) + 0.60)

    while (True):
        nogeenkeer = input("Hier is uw "+ str(keuze) +" met "+ str(hoeveelheid) +" bolletje(s). Wilt u nog meer bestellen? (Y/N) ")
        if (nogeenkeer.lower() == "y"):
            break
        elif(nogeenkeer.lower() == "n"):
            end = True
            break
        else:
            imsorry()
            continue


    if (end == True):
        break
    else:
        continue




hoornkosten = (float(hoorncounter * 1.25))
bakjekosten = (float(bakjecounter) * 0.75)
bolkost = (float(hoeveelheidoplsaan) * 1.10)
totaaluitrekeningh = (float(hoeveelheidoplsaan) * 1.10 + float(hoornkosten) + float(toppingkosten))
totaaluitrekeningb = (float(hoeveelheidoplsaan) * 1.10 + float(bakjekosten) + float(toppingkosten))
totaaluitrekeningbeide = (float(hoeveelheidoplsaan) * 1.10 + float(bakjekosten) + float(hoornkosten) + float(toppingkosten))

print("------------['Papi gelato']------------")
print("")
print("Bolletjes        "+ str(hoeveelheidoplsaan) +" x €1.10   = €"+ str(round(bolkost, 2)))
if (heefthornbesteld == True and heeftbakjebesteld == True):
    hoorncalc()
    bakjecalc()
    toppings()
    bonnetjeeinde()
    print("Totaal                       = €"+ str(round(totaaluitrekeningbeide, 2)))
elif (heefthornbesteld == True):
    hoorncalc()
    toppings()
    bonnetjeeinde()
    print("Totaal                       = €"+ str(round(totaaluitrekeningh, 2)))
elif (heeftbakjebesteld == True):
    bakjecalc()
    toppings()
    bonnetjeeinde()
    print("Totaal                       = €"+ str(round(totaaluitrekeningb, 2)))
