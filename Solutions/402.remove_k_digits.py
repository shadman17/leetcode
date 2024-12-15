# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:

#         length = len(num)

#         stack = []

#         for i in range(length):
#             while stack and k>0 and stack[-1] > num[i]:
#                 stack.pop()
#                 k -= 1
#             stack.append(num[i])

#         if k > 0:
#             stack = stack[:len(stack) - k]

#         result = "".join(stack).lstrip("0") 

#         return result if result else "0"
    
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k == n:
            return '0'
        st = []
        for digit in num:
            while k > 0 and st and st[-1] >= digit:
                st.pop()
                k -= 1
            st.append(digit)
        while k > 0:
            st.pop()
            k -= 1
        while st and st[0] == '0':
            st.remove('0')
        res = ''.join(st)
        return res if st else '0'

    
s = Solution()
print(s.removeKdigits(num = "1432219", k = 3))
print(s.removeKdigits(num = "10", k = 1))
print(s.removeKdigits(num = "1173", k = 2))
print(s.removeKdigits(num = "1234", k = 2))
print(s.removeKdigits(num = "12", k = 2))