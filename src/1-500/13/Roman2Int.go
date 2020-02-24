package main

var mapping map[rune]int = map[rune]int{
	'M': 1000,
	'D': 500,
	'C': 100,
	'L': 50,
	'X': 10,
	'V': 5,
	'I': 1,
}

func romanToInt(roman string) int {
	result := 0
	prev := 4000
	for _, r := range roman {
		i := mapping[r]
		if prev < i {
			result += (i - 2*prev)
		} else {
			result += i
		}
		prev = i
	}
	return result
}

func main() {
	println(romanToInt("MMMXCIX"))
}
