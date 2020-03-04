class Solution {
    public int lengthOfLastWord(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        s = s.trim();
        int pos = s.length() -1;
        while(pos >= 0) {
            if (s.charAt(pos) == ' ') {
                break;
            }
            pos--;
        }
        return s.length() - pos - 1;
    }
}