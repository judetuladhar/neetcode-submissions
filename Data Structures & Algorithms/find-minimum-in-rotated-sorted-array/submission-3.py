class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        if nums[start] <= nums[end]:
            return nums[start]

        while nums[start] > nums[end]:
            start += 1
            end -= 1
            # prev end for right side?
        
        return min(nums[start], nums[end + 1])
