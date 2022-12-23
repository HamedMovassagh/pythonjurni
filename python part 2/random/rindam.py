import random

x=random.randint(1,6)
y=random.random()

mylist=['rock','paper','sessior']
z=random.choice(mylist)


card=[1,2,3,4,5,6,7,8,9,10,"j","q","k","a"]
random.shuffle(card)

print(card)