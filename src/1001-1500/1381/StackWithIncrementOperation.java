class CustomStack {

    Stack<Integer> stack = new Stack<Integer>();
    private int size;

    public CustomStack(int maxSize) {
        size = maxSize;
    }

    public void push(int x) {

        if (stack.size() < size) {
            stack.push(x);
        }
    }

    public int pop() {

        if (stack.size() > 0) {
            return stack.pop();
        } else {
            return -1;
        }
    }

    public void increment(int k, int val) {
        if (k >= stack.size()) {
            for (int i = 0; i < stack.size(); i++) {
                stack.set(i, stack.get(i) + val);
            }
        } else {
            for (int i = 0; i < k; i++) {
                stack.set(i, stack.get(i) + val);
            }
        }
    }

}

/**
 * Your CustomStack object will be instantiated and called as such: CustomStack
 * obj = new CustomStack(maxSize); obj.push(x); int param_2 = obj.pop();
 * obj.increment(k,val);
 */