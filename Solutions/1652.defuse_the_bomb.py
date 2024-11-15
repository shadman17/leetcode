from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        length = len(code)
        total = 0
        arr = [0] * length
        if k >= 0:
            total = sum(code[:k])
            # print(total)

            for i in range(length):
                total -= code[i]
                total += code[(i + k) % len(code)]
                arr[i] = total

        else:
            k = -k
            code = code[::-1]
            # print(k, code)
            total = sum(code[:k])
            for i in range(length):
                total -= code[i]
                total += code[(i + k) % len(code)]
                arr[i] = total

            arr = arr[::-1]

        return arr


s = Solution()
print(s.decrypt(code=[5, 7, 1, 4], k=3))  # [12,10,16,13]
print(s.decrypt(code=[2, 4, 9, 3], k=-2))  # [12, 5, 6, 13]
