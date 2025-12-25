class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total_apple = sum(apple)

        for i in range(len(capacity)):
            total_apple -= capacity[i]
            if total_apple <= 0:
                return i + 1
