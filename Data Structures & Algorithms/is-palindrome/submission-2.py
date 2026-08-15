class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = []
        for c in s:
            if c.isalnum():
                cs.append(c.lower())
        s = "".join(cs)

        print(s)

        return s == s[::-1]

        if len(s)%2 != 0:
            return False

        l, r = 0, len(s)-1 

        while l<r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            
            if s[l] != s[r]:
                return False
            
            l+=1
            r-=1
        return True

            


        