import random


print("Enter User Choice:\n 1 - Rock \n 2 - Paper \n 3 - Scissor")

choice=int(input("Enter the User Choice: "))

while choice>3 or choice<1:
    choice=int(input('Enter a valid choice please '))


if choice==1:
    choice_name="Rock"

elif choice==2:
    choice_name="Paper"

else :
    choice_name="Scissor"

print("User Choice is:" +choice_name)

comp_choice=random.randint(1,3)

if comp_choice == 1:
    comp_choice_name = 'rocK'
elif comp_choice == 2:
    comp_choice_name = 'papeR'
else:
    comp_choice_name = 'scissoR'


print("Computer Choice is:"+comp_choice_name)


#Check the draw condition
if choice==comp_choice:
    print("Draw")

#winning Condtions for paper

if(choice==1 and comp_choice==2):
    print("Paper Win")

elif (choice==2 and comp_choice==1):
    print("Paper Win")



#winning Condtions for rock
    
if (choice==1 and comp_choice==3):
    print("Rock Win")

elif(choice==3 and comp_choice==1):
    print("Rock Win")

#winning Condtions for scissor
    
if (choice==2 and comp_choice==3):
    print("Scissor Win")

elif(choice==3 and comp_choice==2):
    print("Scissor Win")
