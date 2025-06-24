class Solution:
    def majorityElement(self, arr: List[int]) -> int:

        
        arr.sort()
        n= len(arr)
        return arr[n//2]