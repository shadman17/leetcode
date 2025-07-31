class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        x = len(word1)
        y = len(word2)
        length = x if x < y else y

        newlist = []
        p = 0
        for i in range(length):
            newlist.append(word1[p])
            newlist.append(word2[p])
            p += 1

        if p < x:
            while p < x:
                newlist.append(word1[p])
                p += 1

        else:
            while p < y:
                newlist.append(word2[p])
                p += 1

        return ''.join(newlist)