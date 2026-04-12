class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int lo=1,hi=piles[0];
        for(int i=1;i<piles.length;i++)if(piles[i]>hi)hi=piles[i];
        while(lo<hi){
            int m=(lo+hi)/2;
            int c=0;
            for(int i:piles){c+=Math.ceil(i/(double)m);}
            if(c<=h)hi=m;
            else lo=m+1;
        }
        return lo;
    }
}