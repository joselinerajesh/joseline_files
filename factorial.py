num=int(input("enter number"))
fact=1
a=num
b=num
for i in range(1,num):
    fact=a*(b-1)
    a=fact
    b=b-1

print(num, "! factorial is",fact)


