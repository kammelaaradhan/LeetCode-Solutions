# Day 4: LeetCode Practice
# Problem: 1186. Maximum Subarray Sum with One Deletion
# Difficulty: Medium
# Status: Accepted (38/38 test cases passed)
# Runtime: 37ms (Beats 75.38%)
# Memory: 26.20 MB (Beats 58.97%)
# Date: Nov 24, 2025

from typing import List
import math

class Solution:
    """
    Solves the Maximum Subarray Sum with One Deletion problem
    using Dynamic Programming.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        
        # dp_no_del: max subarray sum ending at current index, with NO deletion so far.
        # This is essentially Kadane's algorithm.
        dp_no_del = arr[0]
        
        # dp_one_del: max subarray sum ending at current index, with EXACTLY ONE deletion so far.
        # This is initialized to a very small number because the first element cannot be deleted
        # (resulting subarray must be non-empty, so deleting arr[0] leads to an empty subarray).
        # We can also initialize it with a value that represents 'not yet possible/valid'
        # or just arr[0] and handle the logic carefully. Let's use arr[0] as a starting point,
        # but the one_del calculation must be based on the previous dp_no_del (which can be a single element).
        # A simpler way is to consider it only valid from index 1.
        
        # Initializing dp_one_del to negative infinity for the first element,
        # as a subarray starting and ending at arr[0] cannot have a deletion and still be non-empty.
        dp_one_del = -math.inf
        
        # The overall result must be at least the single largest element.
        max_sum = arr[0]
        
        for i in range(1, n):
            current_val = arr[i]
            
            # --- Calculate the NEW dp_one_del (must be calculated before dp_no_del is updated) ---
            # dp_one_del update has two options:
            # 1. Delete the current element arr[i]. The sum is the best NO-deletion sum ending at i-1. (dp_no_del_prev)
            # 2. Extend the previous one-deletion sum (dp_one_del_prev + arr[i]).
            # Note: math.inf for dp_one_del_prev ensures we only consider valid non-inf sums.
            new_dp_one_del = max(dp_no_del, dp_one_del + current_val)
            
            # --- Calculate the NEW dp_no_del ---
            # Standard Kadane's: either start new at current_val, or extend previous subarray.
            new_dp_no_del = max(current_val, dp_no_del + current_val)
            
            # --- Update DP states for the next iteration ---
            dp_no_del = new_dp_no_del
            dp_one_del = new_dp_one_del
            
            # --- Update the global maximum sum ---
            # The maximum sum can come from either a subarray with no deletion, or one with one deletion.
            max_sum = max(max_sum, dp_no_del, dp_one_del)
        
        return max_sum
