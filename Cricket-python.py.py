import random
l=[1,2,3,4,5,6]
l99=["head","tail"]
l100=["bat","ball"]
z=input("Please enter your name: ")
print(f"Hey {z}!, lets play a game of cricket")
print("Firstly, lets have a toss...")
y=input("head or tail: ")
# x=int(input("Now, choose a number from 1 to 6:"))
l1=None
l2=None
w1=None
w2=None
r1=random.choice(l99)
r2=random.choice(l100)
rm=random.choice(l)
if y=="head":
    if (r1==y):
        w1=("You won the toss!")
    else:
        l1=("You lost the toss...")
elif y=="tail":
    if (r1==y):
        w2=("You won the toss!")
    else:
        l2=("You lost the toss...")
if l1==None:
    pass
else:
    print(l1)
if l2==None:
    pass
else:
    print(l2)
if w1==None:
    pass
else:
    print(w1)
if w2==None:
    pass
else:
    print(w2)
if y=="head":
    if w1==("You won the toss!"):
        a=input("bat or ball: ")
    else:
        print("The computer chose",r2)
elif y=="tail":
    if w2==("You won the toss!"):
        a=input("bat or ball: ")
    else:
        print("The computer chose",r2)
if w1==("You won the toss!") or w2==("You won the toss!"):
    if a=="bat":
        pass
    if a=="ball":
        pass
else:
    if r2=="bat":
        pass
    if r2=="ball":
        pass
