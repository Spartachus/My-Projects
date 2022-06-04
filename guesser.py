import random

Sec_num = random.randint(0, 10)
attempts = 4 
msg = 'You Lost!'   

while attempts > 0:
    user_input = int(input('Guess a number: '))

    if user_input == Sec_num:
        msg = 'You Won!'
        break
    if user_input < Sec_num:
        print("Your choice is too small")
        print(f'Try again! {attempts} attempt left.')
        attempts -= 1

    if user_input > Sec_num:
        print("your choice is too big")
        print(f'Try again! {attempts} attempt left.')
        attempts -= 1
print(msg)