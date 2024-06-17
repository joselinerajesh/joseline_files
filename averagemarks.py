a=int(input("enter english mark:"))
b=int(input("enter tamil mark:"))
c=int(input("enter maths mark:"))
d=int(input("enter science mark:"))
e=int(input("enter social mark:"))
avg=(a+b+c+d+e)/5
if(avg<35):
    print("additional class is required")
else:
    print("you are gud")
