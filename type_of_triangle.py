class solution:
    def type_of_tri(self,n):
        n.sort()
        if n[0]>=n[1]+n[2]:
            return "none"
        if n[0]==n[2]:
            return "equilateral"
        if n[0]==n[1] or n[1]==n[2]:
            return "isosecles"
        return "scalene"
n=list(map(int,input("enter list ").split()))
sol=solution()
print(sol.type_of_tri(n))