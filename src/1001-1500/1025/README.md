# 题目
## Divisor Game

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

Note:

1 <= N <= 1000

# 级别 
Easy



# 解题思路

prove it by two steps:

if Alice will lose for N, then Alice will must win for N+1, since Alice can first just make N decrease 1.
for any odd number N, it only has odd factor, so after the first move, it will be an even number
let's check the inference
fisrt N = 1, Alice lose. then Alice will must win for 2.
if N = 3, since all even number(2) smaller than 3 will leads Alice win, so Alice will lose for 3
3 lose -> 4 win
all even number(2,4) smaller than 5 will leads Alice win, so Alice will lose for 5
...

Therefore, Alice will always win for even number, lose for odd number

因为之前不管产生了多少Move, 最后都是只能 在 2 和 1 之间 Move one step,选择2 的人就win,1 的就lose.



# 算法归类
math

