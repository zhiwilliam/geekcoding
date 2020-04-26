# 题目
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

# 级别 
Easy

# 解题思路
The core strategy is to identify numbers that are multiples of 3 or 5, and replacing them with the corresponding strings. All solutions seem to focus on making this process as efficient as possible.

Python's list comprehension is a good choice for this problem.