from collections import Counter

class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

t = Solution1()
print(t.isIsomorphic(s = "bbbaaaba", t = "aaabbbba"))
print(t.isIsomorphic(s = "egg", t = "add"))
print(t.isIsomorphic(s = "paper", t = "title"))
print(t.isIsomorphic(s = "foo", t = "bar"))
print(t.isIsomorphic(s = "badc", t = "baba"))

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        new_dict = {}
        new_dict2 = {}
         
        for i, char in enumerate(s):
            # print(i, char)
            if char not in new_dict:
                new_dict[char] = t[i]
   
            else:
                if new_dict[char] != t[i]:
                    return False

        for i, char in enumerate(t):
            # print(i, char)
            if char not in new_dict2:
                new_dict2[char] = s[i]
   
            else:
                if new_dict2[char] != s[i]:
                    return False

        return True


s = Solution()
print(s.isIsomorphic(s = "bbbaaaba", t = "aaabbbba"))
print(s.isIsomorphic(s = "egg", t = "add"))
print(s.isIsomorphic(s = "paper", t = "title"))
print(s.isIsomorphic(s = "foo", t = "bar"))
print(s.isIsomorphic(s = "badc", t = "baba"))

