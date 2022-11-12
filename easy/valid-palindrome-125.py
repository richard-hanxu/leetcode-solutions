class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
        s = s.lower()
        s = ''.join(filter(lambda c: c in alphabet, s))
        
        p1 = 0
        p2 = len(s) - 1
        while(p1 < p2):
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True