nums = [1,2,3,4,5,6,7]
nums2 = [1, 2, 3, 4, 5,6,7]
nums2 = nums

print(nums)
print(nums2)
nums.append(2401)
print(len(nums))
print(len(nums2))
print(nums)
print(nums2)
   
nums3 = nums[:]
nums3.append(2401)
print(len(nums3))
print(nums3)
