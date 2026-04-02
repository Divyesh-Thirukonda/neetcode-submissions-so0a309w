class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [(math.sqrt((x1)**2 + (y1)**2), i) for i,(x1,y1) in enumerate(points)]
        print(dists)

        heapq.heapify(dists)
        ret = []
        for _ in range(k):
            ret.append(points[heapq.heappop(dists)[1]])
        return ret