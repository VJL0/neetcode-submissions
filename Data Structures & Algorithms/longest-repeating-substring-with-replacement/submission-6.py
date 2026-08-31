class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N=len(s)
        counter={}
        maxCount=0
        
        l=0
        for r, rc in enumerate(s):
            counter[rc]=counter.get(rc, 0)+1

            while (r-l+1)-max(counter.values())>k:
                counter[s[l]]-=1
                l+=1
            
            maxCount = max(maxCount, r-l+1)
        
        return maxCount

        