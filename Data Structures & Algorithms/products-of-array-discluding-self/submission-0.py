class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1] * len(nums)
        right_prod = [1] * len(nums)
        for i in range(1,len(nums)):
            left_prod[i] = nums[i-1] * left_prod[i-1]
        for i in range(len(nums) - 2, -1, -1):
            right_prod[i] = nums[i+1] * right_prod[i+1]

        for i in range(len(nums)):
            nums[i] = left_prod[i] * right_prod[i]


        return nums



