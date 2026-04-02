class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(pos, speed) for pos, speed in zip(position, speed)]
        pair.sort(key = lambda x : -x[0])
        print(pair)
        fleets = []
        for p, s in pair:
            fleets.append((target - p) / s)
            if len(fleets) > 1 and fleets[-1] <= fleets[-2]:
                fleets.pop()

        return len(fleets)