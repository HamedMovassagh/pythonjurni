import random
#import os
# os.system('cls')



while True:
    choices = ['rock', 'paper', 'scissor']
    player = None


    while player not in choices  :
     ai=random.choice(choices)
     player=input("rock ,paper or scissor pick one ").lower()
     if player==ai :           #ai pick rock situation
        print("ai pick :"+ai)
        print("player pik :"+player)
        print("tie !")
     elif player =='rock':
       if ai=='paper' :
        print("ai pick :"+ai)
        print("player pik :"+player)
        print("you lose !")
       elif ai=='scissor' :
        print("ai pick :"+ai)
        print("player pik :"+player)
        print("you win!")
    
     elif player =='scissor':  #ai pick scissor situation
       if ai=='rock' :
        print("ai pick :"+ai)
        print("player pik :"+player)
        print("you lose !")
       elif ai=='paper' :
        print("ai pick :"+ai)
        print("player pik :"+player)
        print("you win!")
    
     elif player =='paper':  #ai pick paper situation
       if ai=='scissor' :
        print("ai pick :"+ai)
        print("player pik :"+player)
        print("you lose !")
       elif ai=='rock' :
        print("ai pick :"+ai)
        print("player pik :"+player)
        print("you win!")

    abbvb=input("play agane [yes//no]").lower()
    print(abbvb)
    if abbvb != "yes":
        break
print("bye")