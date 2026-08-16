class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        l = 0
        seen = set()

        for r, rLetter in enumerate(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(rLetter)
            res = max(res, r-l+1)
        return res
        