from random import shuffle
from tracemalloc import start

sec_num=("1,2,3,4,5,6,7,8,9,0")
sec_num1=shuffle(sec_num)
Guess_count=0
Guess_limit=11
while Guess_count < Guess_limit:
    Guess = int(input("Guess:"))
    Guess_count+=1
    if Guess==sec_num1:
        print("You Won!")
        break
    elif Guess!=sec_num1:
        print("Try Again!")
    




