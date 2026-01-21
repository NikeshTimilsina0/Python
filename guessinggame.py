import random

print("--- Select Difficulty ---")
print("1. Easy   (10 tries, range 1-50)")
print("2. Medium (6 tries,  range 1-100)")
print("3. Hard   (6 tries,  range 1-200)")

while True:
    choice = input("Pick a level (1/2/3): ")
    if choice == '1':
        guess_count, max_range = 10, 50
        break
    elif choice == '2':
        guess_count, max_range = 6, 100
        break
    elif choice == '3':
        guess_count, max_range = 6, 200
        break
    else:
        print("Invalid choice, picking Medium by default.")
        guess_count, max_range = 6, 100
        break


num = random.randint(1, max_range) 
guessed_num = -1
print(f"Type 0 to exit! \nYou have {guess_count} guesses! \nLet's start")
while guessed_num!=0 and guess_count>0:
    try:
        guessed_num=int(input(f"Enter your guess (between 1 and {max_range}): "))
        if guessed_num==0:
            print('Exited')
            break#exit loop if the guess is correct 
        if guessed_num==num:
            print(f'You won! The number was {guessed_num}')
            break
        #Give hints
        elif guessed_num>num:
            print(f'The number is less than {guessed_num}')
        else:
            print(f'The number is more than {guessed_num}')
        guess_count-=1
        if guess_count>0:
            print(f'{guess_count} guesses remaining')
        else:
            print(f'You lose! The number was {num}')
    except ValueError:
        print("Invalid guess! Retry or type '0' to exit")