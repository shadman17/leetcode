from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)

        count_t = Counter(t)        

        return count_s == count_t
    
s = Solution()
print(s.isAnagram(s = "anagram", t = "nagaram"))
print(s.isAnagram(s = "rat", t = "car"))
