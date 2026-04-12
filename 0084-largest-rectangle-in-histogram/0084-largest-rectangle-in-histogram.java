class Solution {
    public int largestRectangleArea(int[] heights) {
        int n=heights.length;
        Stack<Integer> st=new Stack<Integer>();
        int ma=0,i=0;
        while(i<n || !st.isEmpty()){
            if(i<n && (st.isEmpty()||heights[i]>heights[st.peek()]))st.push(i++);
            else{
                int h=heights[st.pop()];
                int w=st.isEmpty()?i:i-st.peek()-1;
                ma=Math.max(ma,h*w);
            }
        }
        return ma;
    }
}