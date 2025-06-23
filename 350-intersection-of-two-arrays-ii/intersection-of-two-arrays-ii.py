class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums1)
        res = []
        for i in nums2:
            if count[i] >0:
                res.append(i) 
                count[i] -= 1
        return res