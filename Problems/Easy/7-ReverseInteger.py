# coding=utf-8
# python3
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        x_ =  int(str(x)[::-1]) if x >= 0 else - int(str(-x)[::-1]) 
        # !!! >= -2147483648
        if x_ < 2147483648 and x_ >= -2147483648:
            return x_
        else:
            return 0

if __name__=='__main__':
    rev = Solution()
    # test case -2147483648 is WA  = =  
    print (rev.reverse(-2147483648))




