nums = [4, 6, 2, 6, 4, 4, 3, 2, 6, 1]
freq = {} # dictionary to store the frequency of each number

# count()
# if key in dict: ignore the value in loop
# dict[key] = value
# logic - counter/frequency dictionary to count the occurrences of each number
# dictionary to store the frequency of each number

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