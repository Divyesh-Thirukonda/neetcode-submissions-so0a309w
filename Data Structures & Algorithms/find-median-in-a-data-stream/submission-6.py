class MedianFinder:

    def __init__(self):
        self.minH = []
        self.maxH = []
        heapq.heapify(self.minH)
        heapq.heapify(self.maxH)
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minH, num)
        heapq.heappush(self.maxH, -num)
        return

    def findMedian(self) -> float:
        startingN = len(self.minH)

        reconMin = self.minH[:]
        reconMax = self.maxH[:]

        minV = 0
        maxV = 0
        print("START")
        while len(self.minH) + len(self.maxH) >= startingN:
            minV = heapq.heappop(self.minH)
            maxV = -heapq.heappop(self.maxH)
            print(minV, maxV)
        print("DONE")

        self.minH = reconMin
        self.maxH = reconMax

        return (minV + maxV) / 2