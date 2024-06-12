class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)

        solution = []

        i = 0
        while i < len(nums):

            if target == nums[i]:
                solution.append(i)
            
            i += 1
            
        return sorted(solution)