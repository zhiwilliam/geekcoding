# 630. Course Schedule III

There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

## Example:

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]

Output: 3

## Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
* First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
* Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
* Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
* The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
 

## Note:

1. The integer 1 <= d, t, n <= 10,000.
2. You can't take two courses simultaneously.

# 分析
这道题并不是207和210题的延续。我们应该用一个全新的视角来考虑这道题。
从题目的描述中我们知道输入是一系列的课程，包括课程的时长以及截至日期。我们的要求是在可能的情况下尽可能多休一些课程。下面是我的一些分析，当然有一些是常识：
1. 先休最紧迫的课程总没有错误。也就是说我们尽可能在先休Deadline近的课，这是个常识。为了达到这个目的，我们需要对输入的课程列表进行排序，按照课程的Dealline的先后顺序排序。
2. 多学小时长的课总是没错的，这样能最多快好省。
3. 当我们在安排课程的时候发现有一门课按现有的安排不能在Dealine前完成的时候。我们有两条思路，一个是直接不上这门课了。但是想想如果这门课是你非常想上的课，那么你只能重新安排你的课程计划。具体说就是在你已经排好的课程中拿掉一个课程，为新的课程腾地方。那么前面挑的课你要割爱哪一门呢？可以有以下的几种情况：
   * 随便挑一门肯定不是一个好的思路，比如你挑出一门课程时长很短的，你腾出来的时间还不够新课的。所以我们想，最低的要求是要挑出一门时长比新课长的课程出来，这样肯定有足够的时间余量。
   * 如果你前面挑出来的课都是小时长的课程，也就是都比你要上的新课时间短的课程，那么你应该怎么做呢？这样情况下，无论你多想上这门新课，看来你也只能割爱了。只能放弃这门新课了。

不难对吧？都是常识。按照上面的分析，我们需要下面的操作：
1. 排序
2. 用一个优先级队列，用来从已有的课中挑出比新课长的课程。
3. 循环在课程列表里从头扫到尾。

# 代码：
``` Python
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        que = []
        cur = 0
        for t, d in courses:
            heapq.heappush(que, -t)
            cur += t
            if cur > d:
                cur += heapq.heappop(que)
        return len(que)
```

## 复杂度：
* 时间复杂度：***O(nlogn)***
* 空间复杂度： ***O(n)***