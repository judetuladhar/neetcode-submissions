class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        ans = []

        for i in nums:
            res[i] += 1

        for i in range(0, k):
            ans.append(max(res, key=res.get))
            res.pop(max(res, key=res.get))

        return ans

