def imsorry():
    print("Sorry, dat snap ik niet")

end = False
hoorncounter = 0
bakjecounter = 0

while (end == False):
    hoeveelheid = ("")
    aantalvraag = ("")
    x = 1
    counter = 0


    print("“Welkom bij Papi Gelato.")
    print("")

    while (True):
        hoeveelheid = input("Hoeveel bolletjes wilt u? ")
        if (int(hoeveelheid.isnumeric()) == False):
            imsorry()
            continue
        elif (int(hoeveelheid) > 8):
            print("Sorry, zulke grote bakken hebben we niet")
            continue
        elif (int(hoeveelheid) == 1,2,3):
            break
        elif (int(hoeveelheid) == 4,5,6,7,8):
            print("Dan krijgt u van mij een bakje met"+ str(hoeveelheid) +"bolletjes")
            break
        elif (int(hoeveelheid.isnumeric()) == True):
            imsorry()
            continue

    while (True):
        aantalvraag = input("Wilt u deze "+ str(hoeveelheid) +" bolletje(s) in A) een hoorntje of B) een bakje? (Hoorn/Bakje) ")
        if (aantalvraag.lower() == "hoorn" ):
            keuze = ("hoorn")
            hoorncounter = hoorncounter + 1
            break
        elif (aantalvraag.lower() == "bakje"):
            keuze = ("bakje")
            bakjecounter = bakjecounter + 1
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
bolkost = (float(hoeveelheid) * 1.10)
totaaluitrekeningh = (float(hoeveelheid) * 1.10 + float(hoornkosten))
totaaluitrekeningb = (float(hoeveelheid) * 1.10 + float(bakjekosten))

print("------------['Papi gelato']------------")
print("")
print("Bolletjes        "+ str(hoeveelheid) +" x €1.10   = €"+ str(bolkost))
if (aantalvraag.lower() == "hoorn"):
    print("Horentje         "+ str(bakjecounter) +" x €1.25   = €"+ str(bakjekosten))
    print("                              ------ +")
    print("Totaal                       = €"+ str(totaaluitrekeningh))
if (aantalvraag.lower() == "bakje"):
    print("Bakje            "+ str(hoorncounter) +" x €0.75   = €"+ str(hoornkosten))
    print("                              ------ +")
    print("Totaal                       = €"+ str(totaaluitrekeningb))