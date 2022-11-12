class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        '''    
        # Merge Sort
        l = nums.copy()
        l.sort()
        
        # Two Pointers
        p1 = 0
        p2 = len(l) - 1
        
        while(p1 < p2):
            sum = l[p1] + l[p2]
            if sum < target:
                p1 += 1
            elif sum > target:
                p2 -= 1
            else:
                ind1 = nums.index(l[p1])
                nums.reverse()
                ind2 = (len(nums) - 1) - nums.index(l[p2])
                return [ind1, ind2]
        