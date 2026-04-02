class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [] #(0, 30), (1, 38)
        sol = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            print(s)
            if s and t > s[-1][1]:
                while s and t > s[-1][1]:
                    sol[s[-1][0]] = (i - s[-1][0])
                    print("popping: ", s.pop(), "for", t)
                s.append((i, t))
            else:
                s.append((i, t))
                print("adding s:", s)
            
        return sol