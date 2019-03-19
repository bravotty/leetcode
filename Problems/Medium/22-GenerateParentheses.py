# coding=utf-8
# python3
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n):
        res = []
        def backtrace(s='', left=0, right=0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrace(s+'(', left+1, right)
            if left > right:
                backtrace(s+')', left, right+1)
        backtrace()
        return res
 
 
if __name__ == '__main__':
    n = 3
    solution = Solution()
    print(solution.generateParenthesis(n))