#216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

```python

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

```

#Analysis
similar to combination Sum series, backtracking

#Source code
```java
class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> ans = new ArrayList<>();
        if (k == 0 || n <= 0) {
            return ans;
        }
        buildList(ans, new ArrayList<>(), 1, n, k);
        return ans;
    }
    
    private void buildList(List<List<Integer>> ans, List<Integer> list, int index, int n, int k) {
        if (list.size() >= k && n > 0) {
            return;
        }
        if (n < 0 && list.size() <= k) {
            return;
        }
        if (n == 0 && list.size() == k) {
            ans.add(new ArrayList<>(list));
            return;
        }
        for (int i = index; i <= 9; i++) {
            list.add(i);
            buildList(ans, list, i + 1, n - i, k);
            list.remove(list.size() - 1);
        }
        return;
    }
}
```
