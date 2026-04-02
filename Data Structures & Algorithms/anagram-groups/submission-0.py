class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:            
        ret = defaultdict(list)
        seenAnagrams = []
        for word in strs:
            curr = {}
            for c in word:
                if c in curr:
                    curr[c] += 1
                else:
                    curr[c] = 1
            item = (curr, word)
            seenAnagrams.append(item)

            # grouping
            key = frozenset(curr.items())
            ret[key].append(word)

        return list(ret.values())
