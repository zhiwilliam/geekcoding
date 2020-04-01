class Solution {
    public int reverse(int x) {
		long y = 0;
		int sign = 1;
		if (x < 0) {
			sign = -1;
			x = -x;
		}
		while (x != 0) {
			y = y * 10 + x % 10;
			if (sign * y > Integer.MAX_VALUE || sign * y < Integer.MIN_VALUE) {
				return 0;
			}
			x /= 10;
		}
		return (int) (y * sign);

	}
}