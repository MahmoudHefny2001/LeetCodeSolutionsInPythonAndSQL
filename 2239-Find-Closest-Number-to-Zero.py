class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for number in nums:
            if abs(number) < abs(closest):
                closest = number
        
        if closest < 0 and abs(closest) in nums:
            closest = abs(closest)

        return closest