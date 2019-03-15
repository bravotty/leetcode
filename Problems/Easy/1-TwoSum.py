# coding=utf-8
# python3
# https://leetcode.com/problems/two-sum/

# index of list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            second_num = target - num
            # search the second
            if second_num in nums:
                second_index = nums.index(second_num)
                if second_index != i:
                    return [i, second_index]

# hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, v in enumerate(nums):
            if v in hash_table:
                return [i, hash_table[v]]
            else:
                hash_table[target - v] = i