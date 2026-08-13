class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            ss = str(sorted(s))
            m.setdefault(ss, []).append(s)
            
        return [value for value in m.values()]