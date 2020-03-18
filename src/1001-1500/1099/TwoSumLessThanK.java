class Solution {
    public int twoSumLessThanK(int[] A, int K) {
        Arrays.sort(A);

        int start = 0;
        int end = A.length - 1;
        int max = -1;

        while (start < end) {
            int sum = A[start] + A[end];

            if (sum >= K) {
                end--;
            } else if (sum < K) {
                max = Math.max(max, sum);
                start++;
            }
        }

        return max;
    }
}