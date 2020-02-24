题目
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

级别
Easy

解题思路
这题非常简单直接
直接loop through这个input list即可，未出现的item存入dictionary，出现过的就从dictionary删掉。
最终dictionary只有一个key，直接返还那个key即可