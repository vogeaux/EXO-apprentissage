from asyncio.windows_events import NULL
import random


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




