import random
game1 = None
a = 2
def game() :
    global game1
    game1 = None
    print ("Jeu du 421. Préparation des dès")
    frist_test=random.randrange(0, 6, 1)
    two_test=random.randrange(0, 6, 1)
    three_test=random.randrange(0, 6, 1)
    print(frist_test)
    print(two_test)
    print(three_test)


    if frist_test + two_test + three_test == 6 or frist_test + two_test + three_test == 12:
        print("gagné")
        game1 = "win"
    else:
        print("perdu")
        game1 = "lose"

while game1 == "win":
    a=+1
    print(a)
    game()