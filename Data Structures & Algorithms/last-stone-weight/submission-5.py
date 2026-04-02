class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        revStones = [-s for s in stones]
        heapq.heapify(revStones)

        while len(revStones) > 1:
            v1 = -heapq.heappop(revStones)
            v2 = -heapq.heappop(revStones)
            if v1 == v2:
                continue
            else:
                res = v1 - v2
                heapq.heappush(revStones, -res)
        if len(revStones) == 1:
            return -revStones[-1]
        return 0
