# Day 3: Maximum Subarray (LeetCode #53)
# Problem: Find the contiguous subarray with the largest sum
# Algorithm: Kadane's Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
# Date: November 23, 2025

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# Example usage:
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6
