import random as r  

print("Welcome to Odd OR Even game! \n")
for i in range(0,3):
    print(i);
print("Get set, go")

while dec1.lower() != "odd" and dec1.lower() != "even" and dec1.lower() != "o" and dec1.lower() != "e":
    dec1=input("Odd or Even (Type in O, E, Odd or Even):  ").lower()
while t1.isnumeric() == False:
    t1=int(input("User Input: "))
t2=r.randint(1,6)
print(f"AI input: {t2}")
toss=t1+t2

if toss%2 == 0:
    dec="even"
else:
    dec="odd"
if dec1==dec:
    play=int(input("Batting(1) or Bowling(2)? "))
else:
    play=r.randint(1,2)
if play==1:
    print("You are batting!")
else:
    print("You are bowling!")
#-----------------------------------------------------------------------------------------------
if play==1:
    runs1=0
    while True:
        while r1.isnumeric() == False:
            r1=int(input("User input: "))
        r2=r.randint(1,6)
        print(f"AI input: {r2}")
        if r1==r2:
            print(f"OUT!!! \nYour Score: {runs1}")
            break
        else:
            runs1+=r1

    print("Bowl and beat AI")
    runs2 = 0
    while runs1>runs2:
        r1 = int(input("User input: "))
        r2 = r.randint(1, 6)
        print(f"AI input: {r2}")
        if r1 == r2:
            print(f"OUT!!! \nAI Score: {runs2}\nYour Score: {runs1}\nYou Won")
            break
        else:
            runs2 += r2
    if runs2>runs1:
        print(f"AI Score: {runs2}\nYour Score: {runs1}\nYou Lost")
#-----------------------------------------------------------------------------------------------
if play==2:
    runs2 = 0
    while True:
        while r1.isnumeric() == False:
            r1 = int(input("User input: "))
        r2 = r.randint(1, 6)
        print(f"AI input: {r2}")
        if r1 == r2:
            print(f"OUT!!! \nAI Score: {runs2}")
            break
        else:
            runs2 += r2
    print("Bat and beat AI")
    runs1 = 0
    while runs2>runs1:
        r1 = int(input("User input: "))
        r2 = r.randint(1, 6)
        print(f"AI input: {r2}")
        if r1 == r2:
            print(f"OUT!!! \nYour Score: {runs1} \nAI Score: {runs2}\nYou Lost!")
            break
        else:
            runs1 += r1
    if runs1>runs2:
        print(f"Your Score: {runs1}\nAI Score: {runs2}\nYou Won!!!")
#-----------------------------------------------------------------------------------------------
