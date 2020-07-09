import random

print("\nROCK, PAPER, SCISSORS!!")

lst = ['Rock', 'Paper', 'Scissors']
play = True
while play:
    print("\n1.Rock\n2.Paper\n3.Scissors")
    try:
        user_in = int(input('Choose one(Enter 1/2/3): '))
        if(user_in>0 and user_in < 4):
            comp_in = random.choice([1,2,3])
            print()
            print('Your choice:',lst[user_in-1])
            print("Computer's choice:",lst[comp_in-1])
            print()
            if user_in == comp_in:
                print("It is a tie")
            elif (comp_in == 1 and user_in == 2) or (comp_in == 2 and user_in == 3) or (comp_in == 3 and user_in ==1):
                print("You win")
            else:
                print("You lose")
            print()
            cont=input("Press y to play again: ")
            if cont != 'y' and cont !='Y':
                play = False
        else:
            print("\nInvalid option. Enter 1, 2 or 3")

    except:
        print("Enter 1, 2 or 3")
