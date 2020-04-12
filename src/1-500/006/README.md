The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

# Appendix by jingdaz
1. Add a Java solution with approach: Visit by Row
2. Idea: 
Visit the characters in the same order as reading the Zig-Zag pattern line by line.

For integer k [0, len),

Characters in row 0 are located at indexes k*(2*numRows-2);
Characters in row numRows−1 are located at indexes k*(2⋅numRows−2)+numRows−1;
Characters in inner row i are located at indexes k*(2*numRows−2)+i and (k+1)(2*numRows−2)−i.
3. Result: 
Runtime: 2 ms, faster than 99.96% of Java online submissions for ZigZag Conversion.
Memory Usage: 39.4 MB, less than 68.09% of Java online submissions for ZigZag Conversion.