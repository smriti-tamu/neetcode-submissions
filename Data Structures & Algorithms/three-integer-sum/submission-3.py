class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = set()
        for i in range(len(nums)):
            new_target = (-nums[i])
            seen = {}
            for j in range(i+1, len(nums)):
                target = new_target-nums[j]
                if target in seen:
                    final.add(tuple(sorted((target, nums[j], -new_target))))
                seen[nums[j]] = j
        return list(final)

        