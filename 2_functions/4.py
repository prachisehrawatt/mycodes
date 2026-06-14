#3 sum problem

def three_sum(nums, len_nums):

    result =[]
    for i in range(len_nums):
        for j in range(i + 1, len_nums):
            for k in range(j + 1, len_nums):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in result:
                        result.append(triplet)
    return result

nums = [0, 0, 0]
len_nums = len(nums)
print(three_sum(nums, len_nums))