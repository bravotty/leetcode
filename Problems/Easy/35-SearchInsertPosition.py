# coding=utf-8
# python3
# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] <= target:
                idx += 1
        return idx


# if __name__=='__main__':
# 	a = [1, 3, 5, 6]
# 	num = 0
# 	idx = 0
# 	for i in range(len(a)):
# 		if num == a[i]:
# 			print(i)
# 		if num >= a[i]:
# 			idx += 1
# 	print (idx)