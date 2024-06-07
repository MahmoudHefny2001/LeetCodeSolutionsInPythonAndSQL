class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = sorted([i**2 for i in nums])

        return squares