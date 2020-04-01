/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Codec {

    // Encodes a tree to a single string.
    // encode to acsii char based
    public String serialize(Node root) {
        StringBuilder sb = new StringBuilder();
        serialize(root, sb);
        return sb.toString();
    }

    private void serialize(Node root, StringBuilder sb) {
        if (root == null) {
            return;
        }
        sb.append((char)(root.val + '0'));
        for (Node child : root.children) {
            serialize(child, sb);
        }
        sb.append('#'); // mark all children of this node serialized;
    }



    // Decodes your encoded data to tree.
    public Node deserialize(String data) {
        if (data == null || data.length() == 0) {
            return null;
        }
        return deserialize(data, new WrapInt(0));
    }

    private Node deserialize(String data, WrapInt index) {
        if (index.getValue() == data.length()) {
            return null;
        }
        Node node = new Node(data.charAt(index.getValue()) - '0', new ArrayList<Node>());
        index.increment();
        while(data.charAt(index.getValue()) != '#') {
            node.children.add(deserialize(data, index));
        }
        index.increment(); // skip the sign

        return node;
    }
}

class WrapInt{
    private int value;
    public WrapInt(int value) {
        this.value = value;
    }

    public int getValue() {
        return this.value;
    }

    public void increment() {
        this.value++;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));