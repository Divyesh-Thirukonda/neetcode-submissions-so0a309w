class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append([value, timestamp])

        # "alice" : [["happy", 1], ["sad", 2]]

    def get(self, key: str, timestamp: int) -> str:
        li = self.hm[key][::-1]
        for i in range(len(li)):
            if timestamp >= li[i][1]:
                return li[i][0]
        return ""
        
