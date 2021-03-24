#Cherilus Sam Bracley
#cherilussambracley@gmail.com
#instagram : @tech5_09


import random


X = 30
#This is a random value 

message= "Welcome \n INSERT YOUR NAME "
USERNAME= input(message)


computerMARK = 0
userMARCK = 0

RULES= "You can put only three values 'ROCK', 'PAPER', 'SCISSORS' if you try to insert other value(s) \n the computer will not take in account what you choose and will still playing Don't forget that you have to put only one among this 3 values for your VALUES that the computer will ask you \n after that, Have fun and try to not loose "

print(RULES)

while X:
    
    USER=input("Insert your value \n " + str ( USERNAME) + "-----")
    CHOICE = ['ROCK', 'PAPER', 'SCISSORS']
    n= random.randint(0,2)
    VALUE= CHOICE[n]
    print(VALUE)


    if  (USER == VALUE):
        print("SAME")


        
    elif (USER =='ROCK' and VALUE == 'PAPER'):
        print("Computer win")
        computerMARK = computerMARK + 1
        userMARCK = userMARCK - 1

    elif (USER =='PAPER' and VALUE == 'ROCK'):
        print("User Win")
        computerMARK = computerMARK - 1
        userMARCK = userMARCK + 1

    elif (USER =='SCISSORS' and  VALUE == 'PAPER'):
        print("User win")

        computerMARK = computerMARK - 1
        userMARCK = userMARCK + 1

    elif (USER =='PAPER' and VALUE == 'SCISSORS'):
        print("Computer win")
        computerMARK = computerMARK + 1
        userMARCK = userMARCK - 1

    elif(USER =='ROCK' and VALUE == 'SCISSORS'):
        print("User win")
        computerMARK = computerMARK - 1
        userMARCK = userMARCK + 1

    elif(USER =='SCISSORS' and VALUE == 'ROCK'):
        print("Computer win")
        computerMARK = computerMARK + 1
        userMARCK = userMARCK - 1

    
        
    if(USER == "close"):
        break


if("-" in str(userMARCK)):
    userMARCK = 0

if("-" in str(computerMARK)):
    computerMARK = 0


print("RESUME \n Computer Mark(s) = " + str(computerMARK) + "\n" + "UserMark(s) = "  + str(userMARCK))


if(userMARCK<computerMARK):
    print("Computer is the winner")

elif(userMARCK == computerMARK):
    print("Equality woaw !!!")

else:
    print(USERNAME + str(" is the winner"))

    
        




