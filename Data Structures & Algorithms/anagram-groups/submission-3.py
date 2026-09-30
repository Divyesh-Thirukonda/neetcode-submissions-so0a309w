class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = defaultdict(list)
        for w in strs:
            key = "".join(sorted(w))
            di[key].append(w)
        return [lis for lis in di.values()]