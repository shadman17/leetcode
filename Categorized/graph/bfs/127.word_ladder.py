from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        hashset = set(wordList)
        q = deque()
        q.append((beginWord, 1))

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                prefix, suffix = word[:i], word[i + 1 :]
                print(f"prefix={prefix} , suffix={suffix}")
                for j in range(97, 123):
                    nxt = prefix + chr(j) + suffix
                    if nxt in hashset:
                        hashset.remove(nxt)
                        q.append((nxt, steps + 1))

        return 0


s = Solution()
print(
    s.ladderLength(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"],
    )
)
