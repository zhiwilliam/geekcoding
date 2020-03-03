class Solution {
    //expande from the center
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }
        int start = 0; // keep the index to remember to start of the substring
        int end = 0; // and the end of the substring
        int maxLen = 0;
        String ans = "";
        for(int i = 0; i < s.length(); i++) {
            int len1 = expandFromCenter(s, i, i);
            int len2 = expandFromCenter(s, i, i + 1);
            int len = Math.max(len1, len2);
            if (maxLen < len) {
                maxLen = len;
                ans = s.substring(i - (len - 1) / 2, i + len / 2 + 1 ); // here is tricky
            }
        }
        return ans;
    }

    private int expandFromCenter(String s, int left, int right) {
        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}