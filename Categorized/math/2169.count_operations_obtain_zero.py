# class Solution:
#     def countOperations(self, num1: int, num2: int) -> int:
#         op = 0
#         while num1 > 0 and num2 > 0:
#             if num1 >= num2:
#                 num1 -= num2
#             else:
#                 num2 -= num1

#             op += 1
        
#         return op
    
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        op = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                op += num1 // num2
                num1 = num1 % num2
            else:
                op += num2 // num1
                num2 = num2 % num1

        return op