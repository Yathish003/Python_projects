print ("NOTE : The password must consist atleast 6 characters\n")

#get the password
password = input("Enter the password : ")

#check for the number of characters

if (len (password) < 6):
    print("The size of password is too small, Try again!")
    exit()

#check for alphabets

is_alpha = False
for _ in password:
   
    if _.isalpha():
        is_alpha = True
        break

if not is_alpha:
    print(" The passowd must contain atleast one Alphabet")
    print("Try again...!")
    exit()

#check for numbers
any_num = False
for a in password:
    
    if a.isdigit():
        any_num = True
        break
    
if not any_num:
    print("The password should contain atlest one Nubmer")
    print("Try again...!")
    exit()

#check for special charactors

spe_char = False

for _ in password:
    if not _.isalpha()  and not _.isdigit():
        spe_char = True
        break

if spe_char is False:
    print("The password should contain atleast 1 special charactor")
    print("Try again...!")
    exit()

print(f"The password '{password}' is accepeted :) \n")