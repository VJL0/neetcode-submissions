class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        res = []
        for i in range(k):
            mx = max(count, key=count.get)
            count.pop(mx)
            res.append(mx)
        return res
