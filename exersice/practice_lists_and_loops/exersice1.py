# Double [2,4,6,8,10]

nums = [2,4,6,8,10]

def double_arr(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]*2
    
    return nums

def double_arr2(nums):
    result = []
    for number in nums:
        result.append(number*2)
    return result



    
print(nums)
print(double_arr2(nums))
double_arr(nums)
print(nums)
