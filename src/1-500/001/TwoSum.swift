
import Foundation
//Note: For mac users, try to execute code in Playgrounds
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var map = [Int: Int]()
        for (i, v) in nums.enumerated() {
            if let j = map[target - v] {
                return [j, i]
            }
            map[v] = i
        }
    }
}


print(Solution().twoSum([2, 7, 11, 15],9))