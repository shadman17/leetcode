from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        result = []

        for i in range(len(operations)):


            if operations[i] == '+':

                val1 = result.pop()
                val2 = result.pop()
                window_sum = int(val1) + int(val2)

                result.append(int(val2))
                result.append(int(val1))
                result.append(window_sum)


            elif operations[i] == 'D':
                val1 = result.pop()
                result.append(int(val1))
                result.append(int(val1) * 2)

            elif operations[i] == 'C':
                result.pop()

            else:
                result.append(int(operations[i]))

        total_sum = sum(result)

        return total_sum

s = Solution()
print(s.calPoints(operations = ["-60","D","-36","30","13","C","C","-33","53","79"]))
print(s.calPoints(operations = ["5","-2","4","C","D","9","+","+"]))
print(s.calPoints(operations = ["1","C"]))