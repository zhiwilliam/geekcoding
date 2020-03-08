# 1371. Find the Longest Substring Containing Vowels in Even Counts

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

```python
Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
```

```python
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
```

```python
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
```

```python
Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
```

# Analysis
Inspired by leetcode discussion, we can use presum to do this question
using a boolean array to store the state of vowels --> as in 0 represents the vowel occurred
even time and 1 represents the vowel occurred odd times.
the state can be key and value is the end index of the potential substring
i.e key can be "00000" no vowels
"10000" only one 'a'
# Source Code
```java
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
```
