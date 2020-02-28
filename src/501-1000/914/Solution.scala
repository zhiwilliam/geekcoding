object Solution {
    def hasGroupsSizeX(deck: Array[Int]): Boolean = {
        deck.groupBy(identity).mapValues(_.length).values.reduce(gcd _) >= 2
    }
    
    def gcd(a: Int, b:Int): Int = if (b == 0) a else gcd(b, a%b)
}