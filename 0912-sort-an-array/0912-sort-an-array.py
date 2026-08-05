class Solution:
    def mergesort(self,nums,p,r):
        if p<r:
            q=(p+r)//2
            self.mergesort(nums,p,q)
            self.mergesort(nums,q+1,r)
            self.merge(nums,p,q,r)
    def merge(self,A,p,q,r):
        l1=[]
        l2=[]
        for i in range(p,q+1):
            l1.append(A[i])
        for i in range(q+1,r+1):
            l2.append(A[i])
        l1.append(float('inf'))
        l2.append(float('inf'))
        i=0
        j=0
        for k in range(p,r+1):
            if l1[i]<=l2[j]:
                A[k]=l1[i]
                i+=1
            else:
                A[k]=l2[j]
                j+=1


    def sortArray(self, nums: List[int]) -> List[int]:
        p=0
        r=len(nums)-1
        self.mergesort(nums,p,r)
        return nums
        