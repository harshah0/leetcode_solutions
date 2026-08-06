class Solution:
    def firstOccurrence(self, nums, target):
        l, h = 0, len(nums) - 1
        ans = -1

        while l <= h:
            mid = l + (h - l) // 2

            if nums[mid] == target:
                ans = mid
                h=mid-1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

        return ans

    def lastOccurrence(self, nums, target):
        l, h = 0, len(nums) - 1
        ans = -1

        while l <= h:
            mid = l + (h - l) // 2

            if nums[mid] == target:
                ans = mid
                l=mid+1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=self.firstOccurrence(nums, target)

        if(first==-1):
            return [-1,-1]
        
        last=self.lastOccurrence(nums, target)

        return [first,last]