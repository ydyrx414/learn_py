# 修改
nums = [1,2,3,4,5,6,7,1,1]
nums[-2] = 44
print(nums)

#添加
nums.append(55)
print(nums)

#插入
nums.insert(5, 7 ** 7)
print(nums)

#删除
del nums[5]
print(nums)

#移除某一特定元素
nums.remove(1)
print(nums)

#弹出元素
poped = nums.pop(-1)
print(poped)
print(nums)
