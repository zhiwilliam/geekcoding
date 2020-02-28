# 914. X of a Kind in a Deck of Cards
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

## Example 1:
```Python
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
```
## Example 2:
```Python
Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
```
## Example 3:
```Python
Input: deck = [1]
Output: false
Explanation: No possible partition.
```
## Example 4:
```Python
Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].
```

## Example 5:
```Python
Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].
```

## Constraints:

* 1 <= deck.length <= 10^4
* 0 <= deck[i] < 10^4

# Analysis

This question is easy. The basic idea is calculating the occurrences of each distinct card in the deck, then getting the greatest common divisor of all the occurrences. If the final GCD is greater than or equal to 2, then we return true; otherwise, return false.

## Note
The Euclid's algorithm is critical for this question. We must remember how to implement the Euclid's algorithm to calculate GCD of two numbers, although we can use the built-in GCD function in Python.