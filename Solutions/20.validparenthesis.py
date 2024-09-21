class Solution:
    def isValid(self, s: str) -> bool:
        newlist = []
        index = 0
        balanced = True
        while index < len(s) and balanced:
            top = ""
            symbol = s[index]
            if symbol in "({[":
                self.push(newlist, symbol)
            else:
                if self.isempty(newlist):
                    balanced = False

                else:
                    top = self.pop(newlist)

                if not self.matches(top, symbol):
                    balanced = False
            index = index + 1

        if balanced and self.isempty(newlist):
            return True
        else:
            return False

    def push(self, newlist, char):
        newlist.insert(0, char)

    def pop(self, newlist):
        return newlist.pop(0)

    def isempty(self, newlist):
        return newlist == []

    def matches(self, open, close):
        opens = "({["
        closes = ")}]"

        return opens.index(open) == closes.index(close)
