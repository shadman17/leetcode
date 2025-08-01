from collections import Counter


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        hashmap = Counter(blocks[:k])
        min_b = k - hashmap["B"]

        for i in range(len(blocks) - k):
            hashmap[blocks[i]] -= 1
            if hashmap[blocks[i]] == 0:
                del hashmap[blocks[i]]
            hashmap[blocks[i + k]] += 1

            count = k - hashmap["B"]
            min_b = min(count, min_b)

        return min_b


s = Solution()
print(s.minimumRecolors(blocks="WBBWWBBWBW", k=7))
print(s.minimumRecolors(blocks="WWWWBBBBB", k=7))
print(s.minimumRecolors(blocks="WBWBBBW", k=2))


"""
class Solution:

	def minimumRecolors(self, blocks: str, k: int) -> int:
		min_cost = cost = blocks[:k].count('W')

		for i in range(k, len(blocks)):
			cost = cost - (blocks[i - k] == 'W') + (blocks[i] == 'W')
			min_cost = min(min_cost, cost)

		return min_cost
"""
