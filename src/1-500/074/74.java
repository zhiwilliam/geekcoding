public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
       if(matrix == null || matrix.length == 0 || matrix[0].length == 0) return false;
       int m = matrix.length;
    
       int n = matrix[0].length;
       int lo = 0; int hi = m * n - 1;
       
       while(lo <= hi){
           int mid = lo + (hi - lo)/2;
           
           int i = mid / n;
           int j = mid % n;
           if(matrix[i][j] == target){
               return true;
           }
           else if(matrix[i][j] < target){
               lo = mid + 1;
           }
           else{
               hi = mid - 1;
           }
       } 
       return false;
    }
}
