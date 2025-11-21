"""
LeetCode Problem #1: Two Sum
Difficulty: Easy
Date Solved: November 21, 2025

Problem Description:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

Time Complexity: O(n)
Space Complexity: O(n)

Approach: Hash Map
- Use a dictionary to store numbers and their indices as we iterate
- For each number, check if (target - current_number) exists in the dictionary
- If found, return the indices; otherwise, add current number to dictionary
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1: {solution.twoSum(nums1, target1)}")  # Expected: [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test 2: {solution.twoSum(nums2, target2)}")  # Expected: [1, 2]
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Test 3: {solution.twoSum(nums3, target3)}")  # Expected: [0, 1]
