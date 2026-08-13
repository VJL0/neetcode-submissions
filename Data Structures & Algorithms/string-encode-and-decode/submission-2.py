class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        return ";;;".join(strs)+";;;"+str(len(strs))

    def decode(self, s: str) -> List[str]:
        l = s.split(";;;")
        if l[-1] == 0:
            return []
        
        return s.split(";;;")[:-1]