from collections import Counter
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)

        for sandwich in sandwiches:
            if cnt[sandwich] > 0:
                cnt[sandwich] -= 1
            else:
                break
        return sum(cnt.values())


s = Solution()
print(s.countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
# print(s.countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[0, 0, 0, 1, 1, 0]))
