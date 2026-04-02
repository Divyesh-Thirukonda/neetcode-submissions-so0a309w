class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter

        counts = Counter(tasks)
        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while q or maxHeap:
            time += 1

            if maxHeap:
                val = heapq.heappop(maxHeap)
                val += 1
                if val:
                    q.append([val, time+n])
            
            if q and q[0][1] == time:
                qval = q.popleft()
                heapq.heappush(maxHeap, qval[0])
        return time




        