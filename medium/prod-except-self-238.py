class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            arr.append(1)
        for i in range(1, len(nums)):
            arr[i] = arr[i - 1] * nums[i - 1]
        p = nums[len(arr) - 1]
        for i in range(len(nums) - 2, -1, -1):
            arr[i] *= p
            p *= nums[i]
        return arr
            
        
        