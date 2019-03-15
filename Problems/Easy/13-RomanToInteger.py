# coding=utf-8
# python3
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        # record 
        record_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        # extract final num
        final_num = record_map[s[len(s)-1]]
        # 0..len(s)-1
        len_ = len(s) - 1
        for i in range(len_, 0, -1):
            front   = record_map[s[i-1]]
            current = record_map[s[i]]
            # XX eg.
            final_num += front if front >= current else -front
        return final_num