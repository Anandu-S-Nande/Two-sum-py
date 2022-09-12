def Sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)) :
            if target - nums[i] == nums[j]:
                return [i,j]

    return None

test = [3,2,4]
target = 6
print(Sum(test, target))