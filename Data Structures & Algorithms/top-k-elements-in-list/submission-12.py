class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = Counter(nums)
        countLi = [[-freq, num] for num, freq in countNums.items()]
        heapq.heapify(countLi)

        sol = []
        for i in range(k):
            v = heapq.heappop(countLi)[1]
            sol.append(v)
        
        return sol
