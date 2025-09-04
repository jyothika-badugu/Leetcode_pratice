class solution:
    def find_cloest(self,x,y,z):
        d1=abs(x-z)
        d2=abs(y-z)

        if d1<d2:
            return 1
        elif d2<d1:
            return 2
        return 0
x=int(input("enter x val :"))
y=int(input("enter y val :"))
z=int(input("enter z1 val :"))
sol=solution()
print(sol.find_cloest(x,y,z))


