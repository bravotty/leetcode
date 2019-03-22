# coding=utf-8
# python3
# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums):
        res = []
        self.DFS(res, [], nums)
        return res

    def DFS(self, res, l, nums):
        if len(nums) == 0:
            res.append(list(l))

        for i in range(len(nums)):
            l.append(nums[i])
            print (nums[:i])
            print (nums[i+1:])
            self.DFS(res, l, nums[:i] + nums[i+1:])
            l.pop()

if __name__=='__main__':
    sol = Solution()
    num = [1, 2, 3]
    res = sol.permute(num)
    print (res)