class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.res = []
        self._combination(0, [])
        self.index = 0

    def _combination(self, ind, arr):
        if len(arr) == self.combinationLength:
            self.res.append("".join(arr))
            return
        for i in range(ind, len(self.characters)):
            arr.append(self.characters[i])
            self._combination(i + 1, arr)
            arr.pop()
        return self.res

    def next(self) -> str:

        if self.index < len(self.res):
            answer = self.res[self.index]
            self.index += 1
            return answer

    def hasNext(self) -> bool:
        return self.index < len(self.res)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
