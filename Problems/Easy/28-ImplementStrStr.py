# coding=utf-8
# python3
# https://leetcode.com/problems/implement-strstr/

class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)

class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        for i in xrange(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle) and haystack[i+j] == needle[j]:
                    j += 1
                if j == len(needle):
                    return i
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
            