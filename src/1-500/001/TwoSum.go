package main

import "fmt"

func twoSumV1(nums []int, target int) []int {
	m := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		part1 := nums[i]
		part2 := target - part1
		if j, ok := m[part2]; ok {
			return []int{j, i}
		}
		m[part1] = i
	}
	return []int{}
}

func twoSumV2(nums []int, target int) []int {
	m := make(map[int]int)
	for i, v := range nums {
		if j, ok := m[target-v]; ok {
			return []int{j, i}
		}
		m[v] = i
	}
	return []int{}
}

func main() {
	a := []int{2, 7, 11, 15}
	fmt.Print(twoSumV1(a, 9))
}
