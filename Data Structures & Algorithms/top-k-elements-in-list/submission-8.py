class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = {}
        for n in nums:
            if n in di:
                di[n] += 1
            else:
                di[n] = 0

        li = [[] for _ in range(len(nums))]

        for n, count in di.items():
            li[count].append(n)
        print(li)

        rem = k
        ret = []
        for i in range(len(li)-1, -1, -1):
            curr = li[i]
            print("c",curr)
            if len(curr) != 0:
                print("cr",curr)
                for el in curr:
                    print(el)
                    ret.append(el)
                    rem -= 1
                    if rem == 0:
                        return ret
        return li


