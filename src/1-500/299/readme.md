# 题目
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

# 级别 
Easy

# 算法口号
Count them one by one, or establish two sets and count each

# 解题思路
The most straight forward solution (and one that's easier to recall in an interview) is making one pass through both arrays in parallel, and add a bull whenever the two digits are equal. For cows, we'll need to store the numbers of appearances of each digit in an array, and increment/decrement the number of appearance of a digit whenever we see that digit. At first it might look like two arrays are needed, but in fact we can use one array and use a positive count to indicate more appearances in `secret` and negative to indicate appearance in `guess`.

The less straight forward, but also fairly intuitive solution is to count the number of bulls, and the number of both bulls and cows. For the number of bulls, we count the number of times `secret[i] == guess[i]`. For the number of both bulls and cows, we take the lesser number of appearances of each digit in either `secret` or `guess`.