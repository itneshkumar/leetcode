# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_array=nums[0]
        current_sum=0
        for i in range(len(nums)):
            if current_sum < 0:
                current_sum =0
            current_sum += nums[i]
            max_sub_array = max(max_sub_array, current_sum)    
        return max_sub_array  
