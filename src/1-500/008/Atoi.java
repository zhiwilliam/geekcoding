class Solution {
    public int myAtoi(String str) {
		if (str == null || str.isEmpty()) {
			return 0;
		}
		
		int len = str.length();
		long y = 0;
		int sign = 1;
		boolean digited = false;
		for (int idx = 0; idx < len; idx++) {
			char c = str.charAt(idx);
			if (!digited && c == ' ') {
				continue;
			}
			if (!digited && c == '+') {
				digited = true;
			}
			else if (!digited && c == '-') {
				sign = -1;
				digited = true;
			}
			else if (c >= '0' && c <= '9') {
                digited = true;
				y = y * 10 + c - '0';
				if (sign * y > Integer.MAX_VALUE) {
					return Integer.MAX_VALUE;
				}
				if (sign * y < Integer.MIN_VALUE) {
						return Integer.MIN_VALUE;
				}
			}
			else {
				break;
			}
		}
		return (int) (y * sign);

	}
}