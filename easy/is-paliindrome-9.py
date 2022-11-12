class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Converts the integer to a String
        '''
        s = str(x)
        p1 = 0
        p2 = len(s) - 1
        while(p1 < p2):
            if not s[p1] == s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
    
        '''
        if x < 0:
            return False
        l = []
        while (x > 0):
            l.append(x % 10)
            x = int(x / 10)
        print(l)
        for i in range(int(len(l)/2)):
            if(not l[i] == l[len(l) - 1 - i]):
                return False
        return True
        '''
            
        