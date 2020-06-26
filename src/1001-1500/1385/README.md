# 1385. Find the Distance Value Between Two Arrays

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Example 1:

```python
Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
```

Example 2:

```python
Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2
```

Example 3:

```python
Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1
``` 

Constraints:

```python
1 <= arr1.length, arr2.length <= 500
-10^3 <= arr1[i], arr2[j] <= 10^3
0 <= d <= 100

```

## 解题思路

按照题意，对于arr1 数组中的每一个元素X1,枚举数组arr2中的每一个元素y1，检查是否对于每一个y1都有|x1-y1|>d, 如果有就加1.

## 代码

```python
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        cnt = 0

        for x in arr1:

            if all(abs(x-y)>d for y in arr2):

                cnt += 1

        return cnt
```
