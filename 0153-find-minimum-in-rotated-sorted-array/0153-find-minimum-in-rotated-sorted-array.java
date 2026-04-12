class Solution {
    public int findMin(int[] nums) {
        int lo=0,hi=nums.length-1;
        while(lo<hi){
            int m=(lo+hi)/2;
            if(nums[m]<=nums[hi])hi=m;
            else lo=m+1;
        }
        return nums[lo];
    }
}