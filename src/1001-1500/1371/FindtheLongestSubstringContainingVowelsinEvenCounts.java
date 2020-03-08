class Solution {
    public int findTheLongestSubstring(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        boolean[] states = new boolean[5];
        Map<String, Integer> map = new HashMap<>();
        map.put(getKey(states), -1); // -1 for computing the length of the string
        int len = 0;
        char[] array = s.toCharArray();
        for (int i = 0; i < array.length; i++) {
            char c = array[i];
            if (c == 'a') {
                states[0] = !states[0];
            }else if (c == 'e') {
                states[1] = !states[1];
            }else if (c == 'i') {
                states[2] = !states[2];
            }else if (c == 'o') {
                states[3] = !states[3];
            }else if (c == 'u') {
                states[4] = !states[4];
            }
            String key = getKey(states);
            if (map.containsKey(key)) {
                len = Math.max(len, i - map.get(key));
            } else {
                map.put(key, i);
            }

        }
        return len;
    }

    private String getKey(boolean[] states) {
        return Arrays.toString(states);
    }
}