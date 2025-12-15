class Solution:
    def isValid(self, s: str) -> bool:
        opens = set(("(", "{", "["))

        stack = []

        for char in s:
            if char in opens:
                stack.append(char)
            
            else:
                if len(stack) == 0:
                    return False

                top = stack[-1]

                if top == "(" and char == ")":
                    stack.pop()

                elif top == "{" and char == "}":
                    stack.pop()

                elif top == "[" and char == "]":
                    stack.pop()

                else:
                    return False

        return True if len(stack) == 0 else False

# class Solution(object):
# 	def isValid(self, s):
#         d = {'(':')', '{':'}','[':']'}
#         stack = []
#         for i in s:
#             if i in d:  # 1
#                 stack.append(i)
#             elif len(stack) == 0 or d[stack.pop()] != i:  # 2
#                 return False
#         return len(stack) == 0 # 3

# class Solution:
#     def isValid(self, s: str) -> bool:

#         opens = ["(", "{", "["]
#         closes = [")", "}", "]"]

#         newlist = []

#         for i in range(len(s)):
#             symbol = s[i]

#             if symbol in opens:
#                 newlist.insert(0, symbol)

#             else:
#                 if newlist == []:
#                     return False

#                 top = newlist.pop(0)

#                 if closes.index(symbol) != opens.index(top):
#                     return False

#         if newlist == []:
#             return True
#         else:
#             return False


s = Solution()
print(s.isValid("(){}]"))
