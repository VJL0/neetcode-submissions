class Solution:
    def reverse(self, x: int) -> int:
        
        MIN = -2147483648
        MAX = 2147483647
        
        res=0
        while x:
            if res>MAX/10 or res<MIN/10:
                return 0
            
            res = res*10 + int(math.fmod(x, 10))
            x = int(x / 10)

        return res