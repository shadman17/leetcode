class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        newlist = []

        while i >= 0 or j >= 0 or carry:
            p = int(a[i]) if i >= 0 else 0
            q = int(b[j]) if j >= 0 else 0

            total = p + q + carry

            carry = total // 2

            newlist.append(str(total % 2))

            i -= 1
            j -= 1

        return "".join(reversed(newlist))


class Solution:
    def bintodec(self, s):
        length = len(s)
        j = length - 1
        ans = 0
        for i in range(length):

            ans += int(s[j]) * pow(2, i)
            j -= 1
        return ans

    def dectobin(self, val):
        ans = ""
        while val:
            ans += str(val % 2)
            val = val // 2

        ans = ans[::-1]
        return ans

    def addBinary(self, a: str, b: str) -> str:
        if a == "0":
            return b
        if b == "0":
            return a

        new_val1 = self.bintodec(a)
        new_val2 = self.bintodec(b)

        new_val = new_val1 + new_val2

        return self.dectobin(new_val)


class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)

        c = a + b
        # print(c)
        c = bin(c)

        return c.strip("0b")


s = Solution1()

print(s.addBinary("1011", "1010"))
