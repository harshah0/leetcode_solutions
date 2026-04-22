import java.util.Arrays;
class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int total_sum=Arrays.stream(nums).sum();
        int curr_max=nums[0],max_sum=nums[0];
        int curr_min=nums[0],min_sum=nums[0];
        for(int i=1;i<nums.length;i++){
            curr_max=Math.max(nums[i],curr_max+nums[i]);
            max_sum=Math.max(max_sum,curr_max);
        }
        for(int j=1;j<nums.length;j++){
            curr_min=Math.min(nums[j],curr_min+nums[j]);
            min_sum=Math.min(min_sum,curr_min);
        }
        if(max_sum<0){
            return max_sum;
        }
        return Math.max(max_sum,total_sum-min_sum);
    }
}