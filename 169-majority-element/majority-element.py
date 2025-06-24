class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        count = {}
        for i in arr:
            count[i]=count .get(i,0)+1
            if count[i] > len(arr)//2:
                return i
        return -1
            