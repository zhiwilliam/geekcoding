package main

import "math"

var mapping map[int][]string = map[int][]string{
	0: []string{"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"},
	1: []string{"X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"},
	2: []string{"C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"},
	3: []string{"M", "MM", "MMM"},
}

func intToRoman(num int) string {

	result := ""
	for i := 3; i >= 0; i-- {
		level := int(math.Pow10(i))
		if r := num / level; r != 0 {
			result += (mapping[i])[r-1]
		}
		num = num % level
	}
	return result
}

func main() {
	println(intToRoman(3099))
}
