#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
#
# A node in the Trie（字典树） contents three informations:
#    1) Is it the end of a whole word?
#         Word `go` can be a part of `goto` and `got`, so charactor chain `g->o->t->o` could present for three words.
#         so a node need a field(`end`) to flaged is it the end of a certain word.
#
#    2) What's the next character(s)?
#         For word `go` could be a part of `goto` or `good`, so for each node needs a Dict structure to store the branches.
#
# @lc code=start
#

from typing import Dict


class Trie:
    class Node:
        def __init__(self, end: bool = False):
            self.end = end
            self.elements: Dict[int, any] = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            if not cur.elements.__contains__(c):
                cur.elements.update({c: self.Node()})
            cur = cur.elements.get(c)
        cur.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
            cur = cur.elements.get(c)
            if cur is None:
                return False
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
            cur = cur.elements.get(c)
            if cur is None:
                return False
        return True


if __name__ == '__main__':
    trie = Trie()

    trie.insert('goto')

    assert(trie.search('go') is False)
    assert(trie.search('got') is False)
    assert(trie.search('goto') is True)
    trie.insert('go')
    assert(trie.search('go') is True)
    trie.insert('got')
    assert(trie.search('got') is True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

