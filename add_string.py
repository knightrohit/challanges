"""
Time/Space complexity = O(max(N1, N2))
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        if not num1 or not num2:
            return num1 or num2
        
        carry = 0
        out = []
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >=0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >=0 else 0            
            val = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            out.append(val)
            p1 -= 1
            p2 -= 1
            
        if carry:
            out.append(carry)

        return ''.join(map(str, out[::-1]))