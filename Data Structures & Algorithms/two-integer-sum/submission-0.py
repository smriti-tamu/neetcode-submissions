from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter_map = defaultdict(int)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in counter_map:
                return [counter_map[diff], i]
            else:
                counter_map[nums[i]]=i

        