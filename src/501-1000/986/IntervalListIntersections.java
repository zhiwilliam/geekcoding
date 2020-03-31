class Solution {
    public int[][] intervalIntersection(int[][] A, int[][] B) {
        List<int[]> list = new ArrayList<>();
        
        if(A == null || A.length == 0 || B == null || B.length == 0)
            return new int[][]{};
        
        int i = 0, j = 0;
        
        while(i < A.length && j < B.length){
            int first = Math.max(A[i][0], B[j][0]);
            int second = Math.min(A[i][1], B[j][1]);
            
            if(second >= first){
                list.add(new int[]{first, second});
            }
            
            
            if (A[i][1] < B[j][1])
                i++;
            else
                j++;
        }
        
        return list.toArray(new int[list.size()][]);
    }
}