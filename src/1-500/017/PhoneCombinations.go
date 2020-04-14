package main

import "fmt"

var mapping map[rune]string = map[rune]string{
	'2': "abc",
	'3': "def",
	'4': "ghi",
	'5': "jkl",
	'6': "mno",
	'7': "pqrs",
	'8': "tuv",
	'9': "wxyz",
}

func backtracing(digits string, res *[]string, accum string) {
	if len(digits) == 0 {
		*res = append(*res, accum)
	} else {
		for _, c := range mapping[rune(digits[0])] {
			backtracing(digits[1:], res, accum+string(c))
		}
	}
}

func letterCombinations(digits string) []string {
	result := []string(nil)
	if len(digits) != 0 {
		backtracing(digits, &result, "")
	}
	return result
}

func main() {
	fmt.Print(letterCombinations("23"))
}
