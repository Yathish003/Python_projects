def ask_player():   
# This function asks the player whether he/she want's to play or not
    a = 'initial'
    while a.lower() != 'y' and a.lower() != 'n':

        a = input("Do you want to play? (Y/N) : ")
        if a.lower() == 'y':
            
            print('-----------------------')
            print("Ok,let's start the game")
            print('-----------------------')
            
            return True
            
            
        elif a.lower() == 'n':
            
            print('-----------------')
            print("Ok! See you later")
            print('-----------------')
            
            return False
            
           
        else:
            print('----------') 
            print("Try again ")
            print('----------') 

def X_O():
# This function allows the user to choose pawn(x/o)
    choice = 'nope'
    while choice.lower() != 'o' or choice.lower() != 'x':
        choice = input("Player 1 enter your coice (X/O) : ")

        if choice.lower() == 'x':
            
            print('------------------------')
            print("ok player 1 you got  'X'")
            print('------------------------')
            
            return 'X'
            
        
        elif choice.lower() == 'o':
            
            print('------------------------')
            print("ok player 1 you got 'O'")
            print('------------------------')
            
            return 'O'

        else:
            print ('--------------------------')
            print ('invalid option, Try again!')
            print ('--------------------------')

def display(a):
#game display board

    print (  a[6]+  '   |   '  +a[7]+ '    |   '  +a[8] )

    print("--------------------")

    print (  a[3]+  '   |   '  +a[4]+ '    |   '  +a[5] )
    
    print("--------------------")
    
    print (  a[0]+  '   |   '  +a[1]+ '    |   '  +a[2] )

def user_ch_list(enter_list,g): 
# Takes the numpad input and marke it on the cell
    a = False
    
    while a is False:
           
        i = (input('choose the place to play, (1-9):'))
        if i.isdigit():
            s = int(i)

            if s in range(1,10):
        
                if enter_list[s-1] == ' ':
                    a = True
                
                    if g == 'X':
                        enter_list[s-1] = 'X'
                
                    else:
                        enter_list[s-1] = 'O'
                
                else: 
                    print('_____________________________________')
                    print("The place is already filled try again")
                    print('-------------------------------------')

            else:
                print('________________________')
                print("out of range, Try again!")  
                print('------------------------')    
        else:
            print('____________')
            print("Enter digits")
            print('------------')
    return enter_list

def check_win(a):
# Check win or not

    
    if a[0:9:3] == ['X','X','X'] or a[0:9:3] == ['O','O','O']  :
        print('___________')
        print("YOU WIN..:)")
        print('-----------')
        exit()
    elif a[1:9:3] == ['X','X','X'] or a[1:9:3] == ['O','O','O']  :
        print('___________')
        print("YOU WIN..:)")
        print('-----------')
        exit()
    elif a[2:9:3] == ['X','X','X'] or a[2:9:3] == ['O','O','O']  :
        print('___________')
        print("YOU WIN..:)")
        print('-----------')
        exit()
    elif a[0:9:4] == ['X','X','X'] or a[0:9:4] == ['O','O','O']  :
        print('___________')
        print("YOU WIN..:)")
        print('-----------')
        exit()
    elif a[2:7:2] == ['X','X','X'] or a[2:7:2] == ['O','O','O']  :
        print('___________')
        print("YOU WIN..:)")
        print('-----------')
        exit()
    elif a[0:3] == ['X','X','X'] or a[0:3] == ['O','O','O']  :
        print('___________')
        print("YOU WIN..:)")
        print('-----------')
        exit()
    elif a[3:6] == ['X','X','X'] or a[3:6] == ['O','O','O']  :
        print('___________')
        print("YOU WIN..:)")
        print('-----------')
        exit()
    elif a[6:9] == ['X','X','X'] or a[6:9] == ['O','O','O']  :
        print('___________')
        print("YOU WIN..:)")
        print('-----------')
        exit()
    else: pass
   


def main():
# The actual game starts from here 

    print("\n")
    print("______________________")
    print("Welcome to Tic Tac Teo")
    print("----------------------")
    print('\n')

    empty_list = [' ']*9
    

    if ask_player():
        print('_________________')
        print("player 1 go first")
        print('------------------')
        choice = X_O()
        print('______________________')
        print("This is the game board")
        print('----------------------')
        display(empty_list)
        print('_____________________________________________________')
        print("Use the number pad on the keyboard to choose the cell")
        print('-----------------------------------------------------')
        a = 0
        
        while a < 9:
            a = a+1
            display(user_ch_list(empty_list,choice))
            check_win(empty_list)

            if choice == 'X':
                choice = 'O'

            else:
                choice = 'X'
                
        if a == 9:
            print("_______")
            print("DRAW..!")
            print("-------")
    
main()