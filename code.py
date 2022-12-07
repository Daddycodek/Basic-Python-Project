class multiplication:
    def multi(self,n):
        for i in range(1,11):
            for j in range(2,n+1):
                print(j,"*",i,"=",i*j,end=" ")
            print(" ")
a=int(input("Enter Sentinel Value:"))
table=multiplication()
table.multi(a)
