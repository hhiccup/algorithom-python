#暴力法做不出来，参考解法：
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 法1 暴力破解 a + b + c
        res = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append(tuple(sorted((nums[i], nums[j], nums[k]))))
        return list(set(res))
