class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        zeroes = 0
        zero_index = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                res = [0] * nums[i]
                if zeroes == 0:
                    zero_index = i
                    zeroes += 1
                else:
                    res = [0] * len(nums)
                    return res
            else:
                product = product * nums[i]
        
        if zeroes == 1:
            res = [0] * zero_index
            res.append(product)
            for i in range (zero_index + 1, len(nums)):
                res.append(0)
            return res
        
        for n in nums:
            if n == 0:
                print("a zero got in here")
            else:
                res.append(product // n)
        return res
        