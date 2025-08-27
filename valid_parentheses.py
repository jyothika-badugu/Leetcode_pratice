class solution:
    def valid_par(self,s):
        while "()" in s or "[]" in s or "{}" in s:
            s=s.replace("()","").replace("[]","").replace("{}","")
        return len(s)==0
s=input("enter Srting: ")
sol=solution()
print(sol.valid_par(s))

