class Solution {
    public int firstUniqChar(String s) {
        if(s == null || s.length() == 0)
            return -1;
        
        int[] arr = new int[26];
        for(char ch : s.toCharArray()){
            arr[ch - 'a']++;
        }
        

        for(int i = 0; i < s.length(); i++){
            if(arr[s.charAt(i) - 'a'] == 1)
                return i;
        }
        
        return -1;
    }
}