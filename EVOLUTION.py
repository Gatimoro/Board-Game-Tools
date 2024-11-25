import random
foodies=[[1,2],[2,0],[2,2],[3,2]]
plays=0
while not plays:
    try:
        plays=int(input("How many players?\n"))
        if plays<2:
            print("retard")
            plays=0  
    except:
        print("retard")
bonus=foodies[plays-2][1]
dice=foodies[plays-2][0]
while True:
    rolls=[]
    for x in range(dice):
        rolls.append(random.randint(1,6))
    print("Rolls:",str(rolls)[1:-1], "+",bonus,"\nTotal:",sum(rolls)+bonus,"food\nPlayer n°"+str(random.randint(1,plays)),"starts")
    while True:
        crux=input()
        if "neo" in crux:
            try:
                top=int(crux[4:])
                neo=random.randint(1,top)
                if neo == top:
                    print("NEOPLASM IS DESTROYED!")
                else:    
                    print("Ability n°"+str(neo),"got destroyed") 
            except:
                print("something went wrong\nTry again")
        elif crux=="aed":
            bonus+=2
            print("The bonus is now bob!".replace("bob",str(bonus)))
        elif "ded" in crux:
            if bonus==foodies[plays-2][1]:
                print("u stupid?")
            else:
                bonus-=2
                print("R.I.P. Aedificator\nCurrent bonus:",bonus)
        else:        
            break        
        continue        
           
                
                
                
                