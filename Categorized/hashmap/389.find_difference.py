class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        hashmap = {}

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1


        for char in t:
            if char not in hashmap:
                return char
            
            else:
                hashmap[char] = hashmap.get(char) - 1
                if hashmap[char] == 0:
                    del hashmap[char]

        return hashmap

s = Solution()
print(s.findTheDifference("abcd", "abcde"))
print(s.findTheDifference("", "a"))
print(s.findTheDifference("aba", "abaa"))