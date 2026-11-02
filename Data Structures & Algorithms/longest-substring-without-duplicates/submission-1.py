"""
input: string

question: how to find logest substring
- count chars from left to right
conditions for longest substring: 
- must have different chars

output: num of char in longest substring

zxyzxyz

z longest = 0, l=0 r=0
zx longest = 2, l=0 r=1
zxy longest = 3, l=0 r=2

zxyz, l=0 r=3, we saw rChar, move l, l=1, we can already inners are already repeat safe

xyzx

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestStringCount = 0
        left = 0
        seenchars = set()
        for right in range(len(s)):

            while s[right] in seenchars:
                seenchars.remove(s[left])
                left+=1


            
            seenchars.add(s[right])
            longestStringCount = max(longestStringCount, right-left+1)
        return longestStringCount






    