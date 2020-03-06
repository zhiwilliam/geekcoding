# 题目
## Valid Number
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
             
# 级别 
Hard

# 算法口号
两个标志位扫描，注意.233合法

# 解题思路
这种字符串处理的题目烦的很，corner case 太多而且题目说的也不清楚，需要注意的是下面几种case (.54343)这种数据是合法的，(.)这个数据是不合法的，323e这种数据是不合法的，e后面需要跟数字，并且还可能有符号．开头结尾可能有空格．<br>

我们可以设置两个计数器，一个用来测试字符串是否能够按照规定的字符走完，另一个用于标记是否出现了非法的case，比如e后面没有跟数据，或者e不能出现在首位，因为比如：1.2e+12这种是科学计数法，表示1.2*(10^12)，所以e之前必须有数据．
