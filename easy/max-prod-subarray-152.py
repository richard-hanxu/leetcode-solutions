class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currProd = nums[0]
        maxProd = currProd
        for i in range(1, len(nums)):
            if currProd == 0:
                currProd = nums[i]
            else:
                currProd *= nums[i]
            maxProd = max(maxProd, currProd)
        currProd = 1
        for i in range(len(nums) - 1, -1, -1):
            if currProd == 0:
                currProd = nums[i]
            else:
                currProd *= nums[i]
            maxProd = max(maxProd, currProd)
        return maxProd
        