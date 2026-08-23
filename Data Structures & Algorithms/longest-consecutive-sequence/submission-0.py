class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_length=0
        for num in seen:
            if num - 1 not in seen:
                start = num
                length = 1
                while start+1 in seen:
                    start=start+1
                    length +=1
                max_length = max(max_length, length)
        return max_length
        