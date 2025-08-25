class solution:
    def len_last_word(self,s):
        word=s.strip().split()
        if not word:
            return 0
        return len(word[-1])
sol=solution()
s=input("Enter String: ")
print(sol.len_last_word(s))