class Solution:
    def twoSum(self,nums , target):
        arr = []

        for i in range(len(nums)):
            arr.append((nums[i],i))

        arr.sort()

        left = 0
        right = len(nums)-1

        while left < right:
            left_value, left_index = arr[left]
            right_value, right_index = arr[right]
            current_sum = left_value + right_value
            if current_sum == target:
                return [left_index, right_index]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

       