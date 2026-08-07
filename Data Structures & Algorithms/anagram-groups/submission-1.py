class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for words in strs:
            count = [0] * 26

            for char in words:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(words)

        return list(groups.values())



        


        
