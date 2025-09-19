class solution:
    def vowelgame(self,s):
        if 'a' not in s and 'e' not in s and 'i' not in s and 'o' not in s and 'u' not in s :
            return False
        return True
s=input("Enter String: ")
sol=solution()
print(sol.vowelgame(s))