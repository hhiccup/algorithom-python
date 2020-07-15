
################### 1 括号生成################


class Solution: #test1  用视频讲的方法
    def generateParenthesis(self, n: int) -> List[str]:
        result = []        
        def recur(p, i, j, result):
            if not i and not j:
                result.append(p)
                return 
            if i:
                recur(p + '(', i - 1, j, result)
            if j > i:
                recur(p + ')', i, j - 1, result)
        recur('', n, n, result)
        return result


#################### 2 爬楼梯 ####################

'''
class Solution: # try1   //超出时间限制。。 思路对的但是写麻烦了。
    
    def fbnc(self, n):
        if n == 1: return 1
        if n == 2: return 2
        return self.fbnc(n - 1) + self.fbnc(n - 2)

    def climbStairs(self, n: int) -> int:
        result = 0      
        result = self.fbnc(n)
        return result


class Solution: # 题解  81% 20% //用列表模拟函数调用，好方法！！
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


class Solution: # 国际站most 法1 Top down - TLE  //也超时
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1 
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution: # 国际站most 法3  O(1) space  
    def climbStairs(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a+b
            a = tmp
        return b


class Solution: #国际站most 法4 Top down + memorization (list)  23% 20% //速度 慢了
    def climbStairs(self, n):
        if n == 1:
            return 1
        dic = [-1 for i in range(n)]
        dic[0], dic[1] = 1, 2
        return self.helper(n-1, dic)
    
    def helper(self, n, dic):
        if dic[n] < 0: #小于0的才计算，否则不计算直接返回结果。
            dic[n] = self.helper(n-1, dic)+self.helper(n-2, dic)
        return dic[n]


class Solution: # test 1  
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


class Solution: # test 2  
    def climbStairs(self, n):
        if n < 3:
            return n
        a, b = 1, 2
        for i in range(n - 2):
            t = b
            b = a + b
            a = t
        return b
'''

class Solution: # test3 数学公式  （这叫动态规划！？？）
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        a = 1
        b = 2
        for i in range(n - 2):
            tmp = a
            a = b
            b = a + tmp
        return b
