class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        [2,3,6,2,4]
        [-2,-2,-3,-4,-6]
        # pretend this reverse [-2,-2,-3,-4,-6]
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
        print(revStones)
        if len(revStones) == 1:
            return -revStones[-1]
        return 0

        # heapq.heappop
        # heapq.heappop

        # do computation

        # if not equal, take -firstPop + secondPop -> res
        # res = -res
        # heappush res back to heap
