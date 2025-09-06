class solution:
    def powerof_four(self,n):
        if n==1:
            return True
        while n>4:
            n/=4
        return (n==4)
n=int(input("enter n value: "))
sol=solution()
print(sol.powerof_four(n))