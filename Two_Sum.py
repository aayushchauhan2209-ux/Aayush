class Solution:
    def twosum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return[nums[i],nums[j]]
                            
S1 = Solution()
print(S1.twosum([5,2,3,7],5))
# Alternative way 
class Sol:
    def sum(self,num,tar):
        A = 0
        lis = []
        for i in  num:
            A = int(tar) - i
            lis.append(A)
        common = set(num)&set(lis)
        Ans = list(common)
        return Ans


S1 = Sol()
print(S1.sum([5,2,3,7],5))
