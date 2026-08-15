class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # check if any tuple already started with the prev a
            if i>0 and a==nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0:
                    l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    # move through dup b cases
                    while l<r and nums[l]==nums[l-1]:
                        l+=1

        return res