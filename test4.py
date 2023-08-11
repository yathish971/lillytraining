from random import *
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  
print("Hey Lets play Rock Paper Scissor\n")
Choice=int(input("Enter the Choice \n 1 Rock \n 2 Paper \n 3 Scissor \n"))
random=randint(1,3)

print("Your Choice ")
if Choice==1:
    print(rock)
elif Choice==2:
    print(paper)
elif Choice==3:
    print(scissors)

print("Computer Choice ")
if random==1:
    print(rock)
elif random==2:
    print(paper)
elif random==3:
    print(scissors)

if Choice==random:
    print("draw")
elif Choice==1:
    if random==2:
        print("************************Sorry************************")
        print("paper win\nComputer Win")
        print(paper)
    else:
        print("************************congratulations************************")
        print("Rock win\nYou Win")
        print(rock)
elif Choice==2:
    if random==1:
        print("************************congratulations************************")
        print("paper wins\nYou Win")
        print(paper)
    else:
        print("************************Sorry************************")
        print("Scissor Wins\nComputer Win")
        print(scissors)
elif Choice==3:
    if random==1:
        print("************************Sorry************************")
        print("Rock Wins\ncomputer Win")
        print(rock)
    else:
        print("************************congratulations************************")
        print("Scissor Wins\nYou Win")
        print(scissors)


