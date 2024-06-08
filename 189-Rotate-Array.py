class Solution:

    def helper(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        
        l, r = 0, len(nums) - 1
        
        self.helper(nums, l, r)
        

        l, r = 0, k - 1
        
        self.helper(nums, l, r)


        l, r = k, len(nums) - 1
        
        self.helper(nums, l, r)


