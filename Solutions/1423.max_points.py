class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        max_score, cursum = sum(cardPoints[:k]), sum(cardPoints[:k])
        l, r = k - 1, len(cardPoints) - 1

        while l >= 0:
            cursum = cursum - cardPoints[l] + cardPoints[r]
            max_score = max(max_score, cursum)
            l -= 1
            r -= 1

        return max_score
