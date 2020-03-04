# 题目
Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
# 级别 
Medium

# 算法口号
排序，深度优先搜索，for loop 跳过相同项

# 解题思路
这道题看似不难但很容易出错。

第一步必须要先排序。
然后我们写一个DFS（深度优先搜索）。在这个DFS里面，我们从一个指定的index开始往后扫面数组。<br>
排序的作用就是当你发现target减去当前值小于0的话，那后面的就不必再看了，肯定是太大了。
这道题还有一个trick的地方就是要跳过相同的值，否则的话就会出现重复结果。

            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, target - nums[i], i + 1, res, path + [nums[i]])
            
这三行是本题关键，注意dfs传入哪些参数。

# 算法归类
<a href="../../../DFS.md">深度优先</a>