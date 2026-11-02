class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIndex = [-1, -1]
        resLen = 0

        def check(l, r):
            nonlocal resIndex
            nonlocal resLen

            while 0<=l and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    resIndex = [l, r]
                    resLen = r-l+1
                l-=1
                r+=1

        for i in range(len(s)):
            check(i, i)
            check(i, i+1)
        
        return s[resIndex[0]: resIndex[1]+1]