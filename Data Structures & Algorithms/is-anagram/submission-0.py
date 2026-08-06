class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {} # hashmap
        
        for char in s:
            if char in count:
               count[char]+=1
            if char not in count:
                count[char]=1
        
        for char in t:
          if char in count:
            count[char]-=1
                
          if char not in count:
             return False   
          if count[char]==0:
            del count[char] 
        return len(count) == 0 

            
            
        
     



        