public class Solution {
    public int numTrees(int n) {
        
        // dp solution
        if(n <= 1) return 1;
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        
        for(int i = 2; i <= n; i++){
            for(int j = 1; j <= i; j++){
                dp[i] += dp[j - 1] * dp[i - j];
            }
        }
        
        return dp[n];
    }
}

/*//Recursive solution: TLE though.....
public class Solution {
    public int numTrees(int n) {
       if (n <= 1) {
            return 1;
        }   
        return numTreesHelper(1, n);
    }
     
    private int numTreesHelper(int start, int end) {
        if (start >= end) {
            return 1;
        }
         
        int totalSum = 0;
        for (int i = start; i <= end; i++) {
            totalSum += numTreesHelper(start, i - 1) * numTreesHelper(i + 1, end);
        }
         
        return totalSum;
    }
}
