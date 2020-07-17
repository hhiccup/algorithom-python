####################### 1 Pow(x, n) ##########################

'''
class Solution: #视频讲过后  分治法
    def myPow(self, x: float, n: int) -> float:   #  O(logn)  O(logn) (递归用了多层栈空间)
        if n < 0:
            x = 1 / x
            n = -n
        
        def helper(x, n):
            if n == 0:
                return 1.0
            #half = helper(x, n / 2) if n % 2 == 0 else helper(x, (n - 1) / 2) # 注意：可以用去商，省去判断。
            half = helper(x, n // 2)   # 注意：//是取商 ； / 是正常除法，会得到小数
            return half * half if n % 2 == 0 else x * half * half
        return helper(x, n)
'''
class Solution: #看题解的迭代法 （可转换成二进制角度）
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        if x == 0.0: return 0.0
        if n < 0: 
            n = -n
            x = 1 / x
        while n:
            if n % 2:
                res *= x
            x *= x
            n = n // 2
        return res 




##################### 2 
