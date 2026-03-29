class Solution:
    def twoSum(self,nums , target):

        di = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in di:
                return di[diff],i
            di[j] = i
        return[]
       