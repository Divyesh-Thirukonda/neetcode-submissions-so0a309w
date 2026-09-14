class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        li = []
        for p in points:
            li.append((math.sqrt(p[0]**2 + p[1]**2), p[0], p[1]))
        
        heapq.heapify(li)
        res = []
        for _ in range(k):
            popped = heapq.heappop(li)
            res.append(popped[1:])
        print(li)
        return res