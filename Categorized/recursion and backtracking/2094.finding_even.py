class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()

        def find_number(s, used):
            if len(s) == 3:
                num = int(s)
                if num % 2 == 0 and s[0]!='0':
                    res.add(num)
            
                return
            
            for i in range(len(digits)):
                if used[i]:
                    continue
                
                used[i] = True
                find_number(s + str(digits[i]), used)
                used[i] = False

        find_number("", [False] * len(digits))
        return sorted(res)
    
# class Solution:
#     def findEvenNumbers(digits):
#         result = set()       # store unique valid numbers
#         n = len(digits)

#         def backtrack(path, used):
#             # If we built 3 digits → check and add
#             if len(path) == 3:
#                 # no leading zero AND number is even
#                 if path[0] != 0 and path[-1] % 2 == 0:
#                     num = path[0] * 100 + path[1] * 10 + path[2]
#                     result.add(num)
#                 return

#             for i in range(n):
#                 # skip used digits
#                 if used[i]:
#                     continue

#                 # mark digit as used and recurse
#                 used[i] = True
#                 backtrack(path + [digits[i]], used)
#                 used[i] = False  # unmark

#         # run recursion
#         backtrack([], [False] * n)

#         return sorted(result)