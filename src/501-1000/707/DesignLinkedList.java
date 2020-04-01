class MyLinkedList {
    private int size;
    private Node head;

    /** Initialize your data structure here. */
    public MyLinkedList() {
        size = 0;
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    public int get(int index) {
        if(index >= size)
            return -1;
        
        Node node = head;
        for(int i = 0; i < index; i++)
            node = node.next;
        
        return node.val;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    public void addAtHead(int val) {
        Node tem = head;
        head = new Node(val);
        head.next = tem;
        size++;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    public void addAtTail(int val) {
        
        if(head==null)
            head = new Node(val);
        else{
            Node cur = head;
            while(cur.next!=null)
                cur = cur.next;

            cur.next = new Node(val);
        }

        size++;
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    public void addAtIndex(int index, int val) {
        if(index > size)
            return;
        if(index == 0)
            addAtHead(val);
        else{
            Node cur = head;
            for(int i = 0; i < index - 1; i++){
                cur = cur.next;
            }

            Node temNode = cur.next;
            cur.next = new Node(val);
            cur.next.next = temNode;
            size++;
        }
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    public void deleteAtIndex(int index) {
        if(index >= size)
            return;
        
        if (index == 0) {
            head = head.next;
            return;
        }
        
        Node cur = head;
        for(int i = 0; i < index - 1; i++){
            cur = cur.next;
        }
        
        cur.next = cur.next.next;
        size--;
    }
    
    private void deleteTail(){
        Node cur = head;
        while(cur.next.next!=null)
            cur = cur.next;
        
        cur.next=null;
        size--;
    }
}

class Node{
    int val;
    Node next;
    Node(int val){
        this.val = val;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */