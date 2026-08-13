
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in counter_map:
                return [counter_map[diff], i]
            counter_map[nums[i]]=i

        