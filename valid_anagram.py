from typing import Counter

class solution:
    def anagram(self,s1,s2):
        return Counter(s1)==Counter(s2)
s1=input("enter string1:")
s2=input("enter string2:")
sol=solution()
print(sol.anagram(s1,s2))
