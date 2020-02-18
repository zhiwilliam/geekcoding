# Definition for a Node.


class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def __init__(self):
        self.dict = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        newNode = Node(node.val)
        self.dict[node] = newNode
        for neighbor in node.neighbors:
            if not neighbor in self.dict:
                newNode.neighbors.append(self.cloneGraph(neighbor))
            else:
                newNode.neighbors.append(self.dict[neighbor])

        # The following line is wrong. Why?
        # newNode.neighbors = [self.dict.get(neighbor, self.cloneGraph(neighbor)) for neighbor in node.neighbors]

        return newNode

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node3]
node2.neighbors = [node1, node4]
node3.neighbors = [node1, node4]
node4.neighbors = [node2, node3]
solution = Solution()
solution.cloneGraph(node1)
