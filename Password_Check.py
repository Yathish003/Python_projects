print('\n')
print ("NOTE : The password must consist atleast 6 characters")
print ("       Must contain 1 Number, 1 Alphabet and 1 special char\n")

a = False

while a is False:

#get the password
    password = input("Enter the password : ")

    #check for the number of characters
    if (len (password) < 6):
        print("\nThe size of password is too small, Try again!")
        
    else:
        #check for alphabets
        is_alpha = False
        for _ in password:
   
            if _.isalpha():
                is_alpha = True
                a = True
        if not is_alpha:
            print("\nUse one Alphabet too")
            

         #check for numbers
        any_num = False
        for a in password:
    
            if a.isdigit():
                any_num = True
        if not any_num:
            print("\nNo numerical valuse")
            
        
        #check for special charactors
        spe_char = False

        for _ in password:
            
            if not _.isalpha()  and not _.isdigit():
                spe_char = True

        if spe_char is False:
            print("\nspecial charactor is missing")
            
    
    if spe_char and any_num and is_alpha:
        a = True
    else:
        print("\nTry again...!")
        a=False
            
print(f"\nThe password '{password}' is accepeted :) ")      
        

