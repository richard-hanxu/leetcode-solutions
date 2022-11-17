def test(nums):
    l = len(nums)
    currentMax = max(nums)  
    count = 0
    sum = 0
    while(count < l):
        if sum > 0:
            if nums[count] < 0:
                currentMax = sum if sum > currentMax else currentMax
            sum += nums[count]
            sum = 0 if sum < 0 else sum
        elif nums[count] > 0:
            sum += nums[count]    
        count += 1
        if sum > 0:
            return max(sum, currentMax)
        else:
            return currentMax

print(test([5, 4, -1, 7, 8]))