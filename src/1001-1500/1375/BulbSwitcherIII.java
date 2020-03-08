class Solution {
    public int numTimesAllBlue(int[] light) {
        if (light == null || light.length == 0) {
            return 0;
        }
        int rightMost = 0;
        int ans = 0;
        for (int i = 0; i < light.length; i++) {
            rightMost = Math.max(light[i], rightMost);
            if (rightMost == i + 1) {
                ans++;
            }
        }
        return ans;
    }
}