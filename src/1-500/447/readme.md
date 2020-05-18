# 题目
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

# 级别 
Easy

# 解题思路
I don't know for sure, but `O(n^2)` time is probably the best we can do in this case, since we need to compare all points against each other.

For each point, we can find its distance to all other points. When more than 1 other points have the same distance to the point we are currently examining, we can construct at least 2 boomerangs.

If there are 3 other points with the same distance to the current point, we can construct 6 boomerangs (three pairs of points, and their reverses count too). For 4 points, the number of boomerangs is 6*2 = 12. The series goes: 2, 6, 12, 20, 30, ..., which is equal to n(n-1), where n is the number of points with the same distance to the current point.

We construct a hashmap for each point, where the key is the distance to the current point, and the value is the number of points with that distance. This way, we can compute the number of boomerangs that can be formed by using a particular point as the center.

We sum up the number of boomerangs for each point, which will give the result to the problem.

In the worst case scenario, this is `O(n^2)` space as well.