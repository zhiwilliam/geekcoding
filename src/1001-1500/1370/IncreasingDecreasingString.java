class Solution {
    public String sortString(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }
        int[] count = new int[26];
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }
        StringBuilder ans = new StringBuilder();
        int len = count.length;
        while(ans.length() < s.length()) {
            for (int i = 0; i < len; i++) {
                if (count[i]-- > 0) {
                    ans.append((char)('a' + i));
                }
            }
            for (int i = len - 1; i >= 0; i--) {
                if (count[i]-- > 0) {
                    ans.append((char)('a' + i));
                }
            }
        }
        return ans.toString();
    }
}