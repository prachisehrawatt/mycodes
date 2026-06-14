# 2 sum problm

def two_sum(nums,target,len_nums):
   for i in range(len_nums):
      for j in range(i):
          if nums[i]+nums[j]== target:
              #print("target found")
              return [i,j]
            
nums = [3, 3]
target = 6
len_nums = len(nums)    

print(two_sum(nums,target,len_nums))
