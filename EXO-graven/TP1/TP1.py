import random

def niveau1():

    bot_be_ja = random.randrange(1,5)
    print (bot_be_ja)

    while True:
        try:
            j_nbr=int(input("chosir la jarre sur les 5 jarres: "))
        except:
            print("valeur incorrecte")
            continue
        else:
            break
            
            
    if j_nbr == bot_be_ja:
        print("Piege")
    else :
        print("Gagné")


def niveau2():

    trousseau = 0
    bot_be_ja = random.randrange(1,5)
    print (bot_be_ja)

    while True:
        while True:
            try:
                j_nbr=int(input("chosir la jarre sur les 5 jarres: "))
            except:
                print("valeur incorrecte")
                continue
            else:
                break
                
                
        if j_nbr == bot_be_ja:
            print("Piege")
            trousseau=trousseau-1
            if trousseau < 0:
                print("partie perdu")
        else :
            print("Gagné")
            trousseau=trousseau+1
            if trousseau > 2:
                print("Tu deviens roi du temple")

niveau2()


