class Solution {
    public long maximumHappinessSum(int[] hap, int k) {

        long result=0;
        int n = hap.length;
        Arrays.sort(hap);
        int count=0;
        for(int i=n-1;i>=0;i--)
        {
            if(hap[i]-count<=0 || count==k)
            {
                break;
            }
            result = result+hap[i]-count;
            count++;
        }

        return result;
    }
}