# 255. Verify Preorder Sequence in Binary Search Tree


Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

```python
Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true

```
Follow up:
Could you do it using only constant space complexity?

# Analysis
using a stack to store all the left subtree value, while travel to right subtree, if you find anything
larger than left subtree root, then it's false;

# source code
```java
class Solution {
    //iterative solution
    //using stack to keep left subtrees
    //this is O(N) better than divide and conqur
    public boolean verifyPreorder(int[] preorder) {
        int low = Integer.MIN_VALUE;
        Stack<Integer> stack = new Stack<>();
        for (int val : preorder) {
            if (val < low) {
                return false;
            }
            while(!stack.isEmpty() && stack.peek() < val) {
                low = stack.pop();
            }
            stack.push(val);
        }
        return true;
    }
}
```