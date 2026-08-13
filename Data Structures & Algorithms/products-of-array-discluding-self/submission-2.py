class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        prefix=1
        for i, n in enumerate(nums):
            output[i] = prefix
            prefix*=n
        
        postfix=1
        for i, n in enumerate(nums[::-1]):
            output[-1-i] *= postfix
            postfix*=n

        return output
