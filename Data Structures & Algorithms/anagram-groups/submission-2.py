class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWordMap = defaultdict(list)
        for word in strs:
            sortedWord = str(sorted(word))
            sortedWordMap[sortedWord].append(word)

        groupedAnagrams = []
        for _, group in sortedWordMap.items():
            groupedAnagrams.append(group)

        return groupedAnagrams