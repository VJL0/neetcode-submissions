class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {} # com -> i
        for i in range(len(nums)):
            c = target - nums[i]
            if c in m:
                return [m[c], i] 
            m[nums[i]] = i
            # 4->1
        return [0, 0]