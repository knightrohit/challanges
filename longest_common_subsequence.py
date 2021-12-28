"""
Time/Space complexity = O(m*n)
"""
# Top down approach

from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def get_lcs(i, j):
            
            if i < 0 or j < 0:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + get_lcs(i - 1, j - 1)
            
            else:
                return max(get_lcs(i - 1, j), get_lcs(i, j - 1), get_lcs(i - 1, j - 1))
            
        return get_lcs(len(text1) - 1, len(text2) - 1)