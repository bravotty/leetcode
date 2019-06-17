# coding=utf-8
# python3
# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        strs.sort()
        res = ''
        for i in range(len(strs[0])):
            if i >= len(strs[-1]) or strs[-1][i] != strs[0][i]:
                return res
            res += strs[0][i]
        return res