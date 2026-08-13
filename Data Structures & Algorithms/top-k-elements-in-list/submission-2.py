import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        heap=[]
        for i,freq in count.items():
            heapq.heappush(heap, (freq, i))

            if len(heap)>k:
                heapq.heappop(heap)
        return [i for freq,i in heap]


        


