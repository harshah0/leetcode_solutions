class Solution:
    def shipWithinDays(self, w: List[int], d: int) -> int:
        l=max(w)
        h=sum(w)
        ans=h

        while l<=h:
            mid=l+(h-l)//2
            days=1
            current=0
            for weight in w:
                if current+weight<=mid:
                    current+=weight
                else:
                    days+=1
                    current=weight


            if days<=d:
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans
