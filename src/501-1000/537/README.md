#537. Complex Number Multiplication
```python
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
```
#Analysis
Just simple string processing, try to write neat code

#Source Code

```java
class Solution {
    public String complexNumberMultiply(String a, String b) {
        int[] factorA = getRealAndComplexFactor(a);
        int[] factorB = getRealAndComplexFactor(b);
        int real = factorA[0] * factorB[0] - factorA[1] * factorB[1];
        int complex = factorA[0] * factorB[1] + factorA[1] * factorB[0];
        return String.valueOf(real) + "+" + String.valueOf(complex) + "i";
    }
    
    private int[] getRealAndComplexFactor(String str) {
        
        String[] array = str.split("\\+");
        int real = Integer.parseInt(array[0]);
        int com = Integer.parseInt(array[1].substring(0, array[1].length() - 1));
        return new int[]{real, com};
    }
}
```