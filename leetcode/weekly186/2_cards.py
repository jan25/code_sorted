'''
https://leetcode.com/contest/weekly-contest-186/problems/maximum-points-you-can-obtain-from-cards/
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        i = 0
        prefix_score = 0
        while i < k:
            prefix_score += cardPoints[i]
            i += 1
        i -= 1

        max_score = prefix_score
        suffix_score = 0
        j = len(cardPoints) - 1
        while i >= 0:
            suffix_score += cardPoints[j]
            j -= 1
            prefix_score -= cardPoints[i]
            i -= 1
            max_score = max(max_score, suffix_score + prefix_score)
        
        return max_score
    
