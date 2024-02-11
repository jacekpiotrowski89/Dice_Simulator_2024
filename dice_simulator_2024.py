import os
import random

def dice_sides():
    try:
        while True:
            dice_choice = input('A dice choice(sides): ')
            dice_type = ['4','6','8','10','12','20']
            if dice_choice not in dice_type:
                print('Only: 4, 6 , 8, 10, 12, 20')
            else:
                return dice_choice            
    except:  
         dice_sides()

def dice_number(dice_choice):
    while True:
        try:
            dice_number_choice = input(f'For {dice_choice} dice Enter a quantity(1-100): ')
            dice_number_int = int(dice_number_choice)
            if dice_number_int not in range(1,101):
                print('Only number: min:1 max:100.')
            else:
                return dice_number_choice              
        except ValueError:
            print('Only number: min:1 max:100.')
              
def dice_rolling():
    try:
        while True:
            total = 0
            dice_choice = dice_sides() 
            dice_choice_int = int(dice_choice)
            dice_number_choice = dice_number(dice_choice)
            number_int = int(dice_number_choice)
            if number_int > 1:
                print('Rolls: ', end='')
                for i in range(1, number_int):
                    roll = random.randint(1, dice_choice_int)
                    print(f'{roll}', end=', ')
                    total += roll
                last_roll = random.randint(1, dice_choice_int)
                total += last_roll
                print(f'{last_roll} Total: {total}')     
            else:
                roll =  random.randint(1, dice_choice_int)
                print(f"Roll: {roll}")
            quit1()
    except ValueError:
        print('Dice rolling Value Error')
        dice_number(dice_choice)
   
def quit1():    
    try:
        quit1 = input('\nContinue?(y/n): ' )
        if quit1 == 'n':
            print('GOODBYE from Dice Simulator 2024.\n')
            quit()
        elif quit1 == 'y':
            dice_rolling()
        else:
            print('Continue?(y/n): ') 
    except ValueError:
        print('Quit Value Error')

if __name__ == '__main__':
    os.system('cls')
    print('Dice Simulator 2024\n')
    dice_rolling()

