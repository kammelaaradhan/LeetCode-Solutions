# LeetCode 1494: Parallel Courses II
# Day 6 Achievement
# Difficulty: Hard
# Time Complexity: O(n * 2^n + 2^n * n^k)
# Space Complexity: O(2^n)

from typing import List

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        prereq = [0] * n
        for prev, nxt in relations:
            prereq[nxt - 1] |= 1 << (prev - 1)
        
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            # Find available courses this semester
            available = []
            for i in range(n):
                if not (mask & (1 << i)) and (mask & prereq[i]) == prereq[i]:
                    available.append(i)
            
            m = len(available)
            # Generate all subsets of available courses with size <= k
            for subset in range(1 << m):
                if bin(subset).count('1') == 0 or bin(subset).count('1') > k:
                    continue
                next_mask = mask
                for j in range(m):
                    if (subset >> j) & 1:
                        next_mask |= 1 << available[j]
                dp[next_mask] = min(dp[next_mask], dp[mask] + 1)
        
        return dp[(1 << n) - 1]
