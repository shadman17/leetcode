class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        newarr = []
        count = 0

        for char in s:
            if char == "(":
                newarr.append(char)

            else:
                if newarr:
                    newarr.pop()
                else:
                    count += 1

        return len(newarr) + count
