def subtract(P, Q):
     return P - Q

#Take user input
a = input ("Enter the amount you gave: ")
b = input ("Enter the actual price amount: ")

if a == b :
    print("You have no change")
elif a > b:
    subtract((a,b))
    print ("You will receive",(a - b))
elif a < b:
    subtract (b,a)
    print("You have to give",(b -a))
else:
    print ("Invalid input")100