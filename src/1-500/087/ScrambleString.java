class Solution {
    public boolean isScramble(String s1, String s2) {
		if (s1 == null || s2 == null || s1.length() != s2.length()) {
			return false;
		}
		if (s1.equals(s2)) {
			return true;
		}
		
		int len = s1.length();
		boolean[][][] map = new boolean[len+1][len+1][len+1];
		
		for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                map[i][j][1] = (s1.charAt(i) == s2.charAt(j));
            }
		}
		for (int n=2; n<=len; n++) {
			for (int i=0; i<=len-n; i++) {
				for (int j=0; j<=len-n; j++) {
					for (int k=1; k<=n && !map[i][j][n]; k++) {
						map[i][j][n] = (map[i][j][k] && map[i+k][j+k][n-k]) 
							|| (map[i][j+n-k][k] && map[i+k][j][n-k]);
					}
				}
			}
		}
		
		return map[0][0][len];
	}
}