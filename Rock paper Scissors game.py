import random
def get.input():
    return input("Make a choice")

def exit.choice():
    return input("Do you want to try again:")

while True:
    Choices = ("rock","paper","scissors")
    choice=random.choice(Choices)
    U_inp = get.input()
    U_inp = U_inp.lower()
    if U_inp == Choices[0]:
        if choice == Choices[1]:
            print(f"AI chooses {choice}")
            print("AI wins")
        else:
            print(f"AI chooses {choice}")
            print("Human wins")
            
        
    elif U_inp == Choices[1]:
        if choice == Choices[2]:
            print(f"AI chooses {choice}")
            print("AI wins")
        else:
            print(f"AI chooses {choice}")
            print("Human wins")
            
    elif U_inp == Choices[2]:
        if choice == Choices[0]:
            print(f"AI choose {choice}")
            print("AI wins")
        else:
            print(f"AI chooses {choice}")
            print("Human wins")
    elif U_inp == choice:
        print('You draw')
            
    play_again=exit.choice()
    if play_again!="y":
        print("You quit")
        break
    
