import random

user_choice=int(input("enter a choice number 1,2,3:"))
if user_choice==1:
    print("your choice : Rock")
elif user_choice==2:
        print("your choice : paper")
else:
    print("your choice : Scissors")
print(user_choice)
computer_choice=random.randint(1,3)
if computer_choice==1:
    print("computer choice:Rock")
elif computer_choice==2:
    print("computer choice:paper")
else:
    print("computer choice:Scissors")
print(computer_choice)
if user_choice==1 and computer_choice==2:
    print("computer winner")
elif user_choice==1 and computer_choice==3:
    print("user winner")
elif user_choice==1 and computer_choice==1:
    print("mosavi")
elif user_choice==2 and computer_choice==1:
    print("user winner")
elif user_choice==2 and computer_choice==2:
    print("mosavi")
elif user_choice==2 and computer_choice==3:
    print("computer winner")
elif user_choice==3 and computer_choice==1:
    print("computer winner")
elif user_choice==3 and computer_choice==2:
    print("user winner")
else: 
    print("mosavi")

