class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        while l < r:
            if l == r - 1:
                return min(nums[l], nums[r])
            if nums[l] < nums[l + ((r - l) // 2)]:
                l += (r - l) // 2 + 1
                if nums[l - 1] > nums[l]:
                    return nums[l]
            else:
                r -= (r - l) // 2
                if nums[l + 1] < nums[l]:
                    return nums[l + 1]
        return min(nums[l], nums[r])
            
