class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        char = word.find(ch)

        if char == -1:
            return word

        result = []
        for i in range(char + 1):
            result.append(word[i])

        s = ""
        while len(result) != 0:
            s += result.pop()

        for i in range(char + 1, len(word)):
            s += word[i]

        return s
