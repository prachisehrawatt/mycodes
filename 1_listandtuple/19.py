nums = [4, 6, 2, 6, 4, 4, 3, 2, 6, 1]
freq = {}

for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for j in range(len(nums)):

    for k in range(j+1, len(nums)):
        if freq[nums[j]] < freq[nums[k]]:
            nums[j], nums[k] = nums[k], nums[j]

        elif freq[nums[j]] == freq[nums[k]]:
            if nums[j] > nums[k]:
                nums[j], nums[k] = nums[k], nums[j]

print(nums)