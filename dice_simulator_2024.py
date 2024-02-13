import os
import random

def dice_sides():
    try:
        while True:
            dice_choice = input('A die choice(sides): ')
            dice_type = ['4','6','8','10','12','20']
            if dice_choice not in dice_type:
                print('Only: 4, 6 , 8, 10, 12, 20')
            else:
                global dice_choice_int
                dice_choice_int = int(dice_choice)
                return dice_choice_int    
    except ValueError:
        print('Value Error')  
         
def dice_number():
    while True:
        try:
            dice_number_choice = input(f'For {dice_choice_int} die Enter a quantity(1-100): ')
            global dice_number_int
            dice_number_int = int(dice_number_choice)
            if dice_number_int not in range(1,101):
                print('Only number: min:1 max:100.')
            else:
                return dice_number_int           
        except ValueError:
            print('Only number: min:1 max:100.')

def add_dice():
    while True:
        try:
            adding_inp = input('Do You want add new die to rolling pool(y/n): ')
            if adding_inp == 'y':
                dice_list.append(dice_choice_int)
                dice_number_list.append(dice_number_int)
                dice_sides()
                dice_number()
            elif adding_inp == 'n':
                dice_list.append(dice_choice_int)
                dice_number_list.append(dice_number_int)
                break
            else:
                print("Only 'y' or 'n'.")
        except ValueError:
            print('Adding Value Error')

def rolling():
    try:
        result = []
        result_end = []
        for y, z in zip(dice_list, dice_number_list):
            result = ([y]*z)
            for x in result:
                dice = random.randint(1,y)
                result_end.append(dice)
        suma = sum(result_end)
        result_end_str = ", ".join(str(i) for i in result_end)
        print(f'Rolls: {result_end_str} Total: {suma}')   
    except:
        print('Error in calculations.')    

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

def dice_rolling():
    global dice_list
    dice_list = []
    global dice_number_list
    dice_number_list = []
    dice_sides()
    dice_number()
    add_dice()
    rolling()
    quit1()

if __name__ == '__main__':
    os.system('cls')
    print('Dice Simulator 2024\n')
    dice_rolling()
