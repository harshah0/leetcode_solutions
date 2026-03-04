class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1=0
        xor2=0
        for i in nums:
            xor1=xor1^i
        for j in range(0,len(nums)+1):
            xor2=xor2^j
        
        return xor1^xor2

