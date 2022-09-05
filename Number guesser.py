import random
while True:
    count=1
    lown=1
    Qown=random.randint(0,10)
    wown=int(input("Input a number:"))
    count=count+1
    lown=lown+1
    if wown == Qown:
        print("You tied")
        count=count+1
    elif wown < Qown:
        print("Your number is less")
        count=count+1
        lown+=1
    if wown > Qown:
        count=count+1
        lown+=1
        print("Your number is more")
    uj=input("Do you want to quit: y/n:")
    if uj =="y":
        print(f"you played {count} games and had {lown} guesses")
        break
    
