/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/
class Solution {
    //using a hashmap to contruct old node to new node mapping
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }
        Map<Node, Node> map = new HashMap<>();
        Node helperHead = head;
        while(helperHead != null) {
            Node copiedNode = map.getOrDefault(helperHead, new Node(helperHead.val));
            map.put(helperHead, copiedNode);
            if (helperHead.next != null) {
                Node copiedNext = map.getOrDefault(helperHead.next, new Node(helperHead.next.val));
                copiedNode.next = copiedNext;
                map.put(helperHead.next, copiedNext);
            }
            if (helperHead.random != null) {
                Node copiedRandom = map.getOrDefault(helperHead.random, new Node(helperHead.random.val));
                copiedNode.random = copiedRandom;
                map.put(helperHead.random, copiedRandom);
            }

            helperHead = helperHead.next;
        }
        return map.get(head);
    }
}