hoeveelheid = ("")
aantalvraag = ("")

def imsorry():
    print("Sorry, dat snap ik niet")

while (True):
    print("“Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
    print("")
    print("Welke smaak ijs wilt u?")
    print("Keuzes smaak: Vanille, vanille, vanille of vanille")
    while (True):
        smaak = input("Smaak: ")
        if (smaak.lower() == "vanille"):
            break
        else:
            print("Die smaak hebben we niet...")
            continue
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
        aantalvraag = input("Wilt u deze "+ str(hoeveelheid) +" bolletje(s) in A) een hoorntje of B) een bakje? (Hoorn/Bakje)")
        if (aantalvraag.lower() == "hoorn" ):
            keuze = ("hoorn")
            break
        elif (aantalvraag.lower() == "bakje"):
            keuze = ("bakje")
            break
        else:
            print("Sorry dat snap ik niet...")
            continue

    while (True):
        nogeenkeer = input("Hier is uw "+ str(keuze) +" met "+ str(hoeveelheid) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)")
        if (nogeenkeer.lower() == "y"):
            break
        elif(nogeenkeer.lower() == "n"):
            print("Bedankt en tot ziens!")
            quit()
        else:
            imsorry()
            continue