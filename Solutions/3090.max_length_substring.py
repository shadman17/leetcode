from collections import Counter, defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        length = len(s)
        start, end = 0, 0
        max_length = 0
        hashmap = dict()

        while end < length:
            
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1

            while hashmap[s[end]] > 2:
                hashmap[s[start]] -= 1


                if hashmap[s[start]] == 0:
                    del hashmap[s[start]]
                
                start += 1

                

            max_length = max(max_length, end - start + 1)
            end +=1 

        return max_length


s = Solution()
print(s.maximumLengthSubstring(s = "bcbbbcba"))
print(s.maximumLengthSubstring(s = "aaaa"))
print(s.maximumLengthSubstring("bcbbbc"))