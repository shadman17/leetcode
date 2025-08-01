from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom = Counter(ransomNote)
        count_magazine = Counter(magazine)

        for key, value in count_ransom.items():
            if count_magazine[key] < count_ransom[key]:
                return False

        return True


s = Solution()
print(s.canConstruct(ransomNote="a", magazine="b"))
print(s.canConstruct(ransomNote="aa", magazine="ab"))
print(s.canConstruct(ransomNote="aa", magazine="aab"))
print(s.canConstruct(ransomNote="abc", magazine="aabbc"))
print(s.canConstruct(ransomNote="abc", magazine="abbd"))
