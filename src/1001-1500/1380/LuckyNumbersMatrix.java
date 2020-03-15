class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {

        List<Integer> list = new ArrayList<>();

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        int m = matrix.length;
        int n = matrix[0].length;

        int[] minIndex = new int[m];
        int[] maxIndex = new int[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] < min)
                    min = matrix[i][j];
            }
            minIndex[i] = min;
            min = Integer.MAX_VALUE;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[j][i] > max)
                    max = matrix[j][i];
            }
            maxIndex[i] = max;
            max = Integer.MIN_VALUE;
        }

        for (int i = 0; i < minIndex.length; i++) {
            for (int j = 0; j < maxIndex.length; j++) {
                if (minIndex[i] == maxIndex[j]) {
                    list.add(minIndex[i]);
                }
            }
        }

        return list;

    }
}