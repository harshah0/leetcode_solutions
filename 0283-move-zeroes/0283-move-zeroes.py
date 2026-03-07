class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        temp1=0
        
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[temp1],nums[i]=nums[i],nums[temp1]
                temp1+=1