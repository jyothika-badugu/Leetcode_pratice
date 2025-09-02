class solution:
    def two_sum(self,nums,target):
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
nums=list(map(int,input("enter list: ").split()))
target=int(input("enter target: "))
sol=solution()
print(sol.two_sum(nums,target))