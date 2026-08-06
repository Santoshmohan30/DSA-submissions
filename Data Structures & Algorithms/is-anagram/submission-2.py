class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}

        for char in s:
            if char in count:
                count[char] += 1
            if char not in count:
                count[char] = 1

        for char in t:
            if char in count:
                count[char] -= 1
            if char not in count:
                return False

        for val in count.values():
            if val != 0:
                return  False 
        return True        


                




         
             