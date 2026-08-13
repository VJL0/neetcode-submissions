class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            ss = "".join(sorted(s))
            m[ss].append(s)
            
        return list(m.values())