class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num = sorted(nums1 + nums2)
        i = len(num)
        if i % 2 == 0:
            Ans_index = int(i/2)
            An = (num[(Ans_index)] + num[Ans_index-1]) 
            Ans = float(An/2)
            print(Ans)

        else:
            Ans_index = int((i + 1) / 2)
            Ans = num(Ans_index-1)
            print(Ans)
        
    
S1 = Solution()
S1.findMedianSortedArrays([1,2,3],[2,3,4])
