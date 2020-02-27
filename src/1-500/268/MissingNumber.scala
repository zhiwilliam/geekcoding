object Solution {
    def missingNumber(nums: Array[Int]): Int = {
        nums.zipWithIndex.map(x=>x._1^x._2).foldLeft(nums.length)(_^_)
    }

    def missingNumber1(nums: Array[Int]): Int = {
        val n = nums.length
        n*(n+1)/2 - nums.sum
    }
}