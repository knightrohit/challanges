"""
Time Complexity = O(N)
Space Complexity = O(1)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        chars = dict()
        size = 0
        min_indx = 0
        max_size = 0
        
        for indx, val in enumerate(s):
            if val not in chars:
                chars[val] = indx
                size += 1
            else:
                e_indx = chars[val]
                if min_indx <= e_indx:
                    min_indx = e_indx + 1
                    size = indx - min_indx + 1
                    chars[val] = indx
                else:
                    size += 1
                    chars[val] = indx
                    
            max_size = max(max_size, size)
            
        return max_size