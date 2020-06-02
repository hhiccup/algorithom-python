'''
class Solution:   #try1 暴力法（ON^2 O1） 正确但超时
    def maxArea(self, height: List[int]) -> int:
        result = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                height_t = min(height[i], height[j])
                area_t = (j - i)* height_t
                result = max(area_t, result)
                #result = max(result, min(height[i], height[j]) * (j-i))
        return result
'''

class Solution:   #try2 双指针（ON O1）  正确但是速度20% 比较慢。
    def maxArea(self, height: List[int]) -> int:
        result = 0
        minarea = 0
        i, j = 0, len(height)-1
        while i < j:
            result = max(result, min(height[i], height[j])* (j - i))
            if height[i] < height[j]:
                i += 1
                while i < j and height[i] < height[i - 1]: i += 1
                continue
            else:
                j -= 1
                while i < j and height[j] < height[j + 1]: j -= 1

        return result
    
    
#########看了别人的， 可以省去那个min函数#####
class Solution:   #test1 双指针（ON O1）  正确 速度90% 
    def maxArea(self, height: List[int]) -> int:
        result = 0
        i, j = 0, len(height)-1
        while i < j:
            if height[i] < height[j]:
                result = max(result, height[i]* (j - i))
                i += 1
                while i < j and height[i] < height[i - 1]: i += 1
                continue
            else:
                result = max(result, height[j]* (j - i))
                j -= 1
                while i < j and height[j] < height[j + 1]: j -= 1
        return result
