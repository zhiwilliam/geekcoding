object Solution {
    implicit class CombinatorialList[A](l: List[A]) {
        def xcombinations(n: Int): List[List[A]] =
            l match {
                case _ :: _ if n == 1 => l.map(List(_))
                case hd :: tl =>
                    tl.xcombinations(n - 1).map(hd :: _) ::: tl.xcombinations(n)
                case _ => Nil
                }
    }
    def combine(n: Int, k: Int): List[List[Int]] = {
        (1 to n).toList.xcombinations(k)
    }
}