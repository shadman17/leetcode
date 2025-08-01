class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        newlist = []

        while i >= 0 or j >= 0 or carry:
            p = int(a[i]) if i >=0 else 0
            q = int(b[j]) if j >=0 else 0

            total = p + q + carry
            
            carry = total // 2

            newlist.append(str(total % 2))

            i -= 1
            j -= 1

        return "".join(reversed(newlist))
    
class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)

        c = a + b
        # print(c)
        c = bin(c)
        
        return c.strip("0b")

s = Solution1()

print(s.addBinary("1011", '1010'))