package main

func min(a, b int) int {
	if a <= b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func maxArea(height []int) int {
	right := len(height) - 1
	left := 0
	area := 0
	for left < right {
		area = max(area, (right-left)*min(height[left], height[right]))
		if height[right] > height[left] {
			left++
		} else {
			right--
		}
	}
	return area
}

func main() {
	///fmt.Print(lengthOfLongestSubstring("abcabc"))
}
