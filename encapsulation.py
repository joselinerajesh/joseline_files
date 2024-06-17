class company():
    def __init__(self):
        self.__companyname="google"  #encapsuled.. becomes private
        

    def companyName(self):
        print(self.__companyname) #can be accessed from outsideS

c1=company()

c1.companyName()

#print(c1.__companyname) cannot be accessed from outside
