# nums =[4,5,6,88,21,30]
# nums.append(13)
# print(nums)
# nums.insert(0,10)
# print(nums)
# nums.remove(5)
# print(nums)
# nums.pop();
# # nums.clear()
# print(nums)
# # print(nums.index(13))
# print(15 in nums)
# nums.sort()
# print(nums)
# nums.reverse()
# print(nums)
# numsCopied = nums.copy()
# print(numsCopied)

nums2 = []
nums =[45,12,33,58,56,44,12,33,58,12]
for item in nums:
    if item not in nums2:
        nums2.append(item)
print(nums)
print(nums2)