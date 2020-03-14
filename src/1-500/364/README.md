# 364. Nested List Weight Sum II
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

```python
Example 1:

Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.
Example 2:

Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
```

#Analysis
1x + 2y + 3z = (3 + 1) * (x + y + z) - (3x + 2y + z);
(3x + 2y + z) = maxDepth * (x + y + z) - weightSumI
#Source Code
```java
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
class Solution {
    private int maxDepth = 0;
    private int flatSum = 0;
    public int depthSumInverse(List<NestedInteger> nestedList) {
        if (nestedList == null || nestedList.size() == 0) {
            return 0;
        }
        int topDownSum = dfs(nestedList, 1);
        return flatSum * (maxDepth + 1) - topDownSum;
    }
    
    private int dfs(List<NestedInteger> nestedList, int curLevel) {
        if (nestedList == null || nestedList.size() == 0) {
            return 0;
        }
        int sum = 0;
        maxDepth = Math.max(curLevel, maxDepth);
        for (NestedInteger each : nestedList) {
            if (each.isInteger()) {
                flatSum += each.getInteger();
                sum += each.getInteger() * curLevel;
            }else {
                sum += dfs(each.getList(), curLevel + 1);
            }
        }
        return sum;
    }
}
```
