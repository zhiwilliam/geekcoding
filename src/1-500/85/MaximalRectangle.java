class Solution {
    public int maximalRectangle(char[][] matrix) {
		if (matrix.length == 0 || matrix[0].length == 0) {
			return 0;
		}

		int n = matrix.length;
		int m = matrix[0].length;

		int[][] heights = new int[n][m];
		int[][] left_boundaries = new int[n][m];
		int[][] right_boundaries = new int[n][m];
		int[][] consecutive_left_boundaries = new int[n][m];
		int[][] consecutive_right_boundaries = new int[n][m];

		for (int j = 0; j < m; j++) {
			heights[0][j] = matrix[0][j] == '0' ? 0 : 1;
		}

		for (int i = 1; i < n; i++) {
			for (int j = 0; j < m; j++) {
				heights[i][j] = matrix[i][j] == '0' ? 0 : heights[i - 1][j] + 1;
			}
		}
		
		for (int i = 0; i < n; i++) {
			left_boundaries[i][0] = 0;
			consecutive_left_boundaries[i][0] = 0;
			right_boundaries[i][m - 1] = m - 1;
			consecutive_right_boundaries[i][m -1] = m - 1;
		}

		// update left boundaries
		for (int i = 0; i < n; i++) {
			for (int j = 1; j < m; j++) {
				if (matrix[i][j-1] == '1') {
					left_boundaries[i][j] = consecutive_left_boundaries[i][j-1];
				} else {
					left_boundaries[i][j] = j;
				}
				consecutive_left_boundaries[i][j] = left_boundaries[i][j];
				if (i >= 1 && matrix[i-1][j] == '1') {
					if (left_boundaries[i-1][j] > left_boundaries[i][j]) {
						left_boundaries[i][j] = left_boundaries[i-1][j];
					}
				}
			}
		}
		
		// update right boundaries
		for (int i = 0; i < n; i++) {
			for (int j = m - 2; j >= 0; j--) {
				if (matrix[i][j+1] == '1') {
					right_boundaries[i][j] = consecutive_right_boundaries[i][j+1];
				} else {
					right_boundaries[i][j] = j;
				}
				consecutive_right_boundaries[i][j] = right_boundaries[i][j];
				if (i >= 1 && matrix[i-1][j] == '1') {
					if (right_boundaries[i-1][j] < right_boundaries[i][j]) {
						right_boundaries[i][j] = right_boundaries[i-1][j];
					}
				}
			}
		}
		
		int maxArea = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				int area = heights[i][j] * (right_boundaries[i][j] - left_boundaries[i][j] + 1);
				if (area > maxArea) {
					maxArea = area;
				}
			}
		}

		return maxArea;
	}

}