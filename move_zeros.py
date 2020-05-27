
#第一次写的： 不知道属于什么法
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count0 = count0 + 1 
            elif count0 != 0:
                nums[i-count0], nums[i] = nums[i], 0
    
    
    
#第二次写： 用了老师教的快慢指针。  36ms    94%   14.3M   7%
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j: nums[i] = 0
                j = j + 1
            
