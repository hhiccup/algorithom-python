class Solution: # try1   //超出时间限制。。 思路对的但是写麻烦了。
    

    def fbnc(self, n):
        if n == 1: return 1
        if n == 2: return 2
        return self.fbnc(n - 1) + self.fbnc(n - 2)

    def climbStairs(self, n: int) -> int:
        result = 0      
        result = self.fbnc(n)
        return result


class Solution: # 题解  815 20% //用列表模拟函数调用，好方法！！
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
            
        num_list = [0] * (n+1)
        num_list[1] = 1
        num_list[2] = 2
        for i in range(3, n+1):
            num_list[i] = num_list[i-1] + num_list[i-2]
        return num_list[-1]

class Solution: # 题解  81% 20% //不使用O（n）的列表空间，用两个元素即可。
    def climbStairs(self, n: int) -> int:
        res = [0,1] # res -> result
        for x in range(n):
            res.append(res[-1] + res[-2])
            res.pop(0)
        return res[-1]


class Solution: # 国际站most 法1 Top down - TLE  //也超出时间限制了。。
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1 
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution: # 国际站most 法3  O(1) space  40%  20% //怎么没有操作两个列表元素那个快？
    def climbStairs(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a+b
            a = tmp
        return b

    
class Solution: # test 1  93%   20% //不错
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(2,n):
            temp = a + b
            a = b
            b = temp
        return b    
