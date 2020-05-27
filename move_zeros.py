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
    return 0
    
    
