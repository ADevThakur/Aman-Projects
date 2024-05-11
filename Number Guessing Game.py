import random
Cnumber = random.randrange(1,101)
Userinput = int(input("user input"))
if Userinput < Cnumber:
                print("Computer number", Cnumber)
                print("your guess is low 😢")
elif Userinput > Cnumber:
                print("Computer number",Cnumber)
                print("your guess is high ✌😎")
else:
                print("Computer number",Cnumber)    
                print("your guess is equal ✌")
