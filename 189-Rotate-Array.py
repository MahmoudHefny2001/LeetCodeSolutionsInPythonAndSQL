class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1 or len(nums) == 0:
            nums = nums
            return

        # Create a new list with the same length as nums
        new = [0] * len(nums)

        k = k % (len(nums))

        j = k

        left = len(nums) - 1

        for i in range(len(nums)):
            new[ (i + k) % len(nums) ] = nums[i]
        
        nums[:] = new
        




