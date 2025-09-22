from collections import Counter
class solution:
    def countmax_freq_ele(self,nums):
        freq=Counter(nums)
        max_freq=max(freq.values())
        return sum(v for v in freq.values() if v==max_freq)
nums=list(map(int,(input("enter list: ").split())))
sol=solution()
print(sol.countmax_freq_ele(nums))