class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr, l, h = 0, 0, len(nums)-1
    
        while curr <= h:
            if nums[curr] == 0:
                nums[l], nums[curr] = nums[curr], nums[l]
                curr += 1
                l += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[curr], nums[h] = nums[h], nums[curr]
                h -= 1  
