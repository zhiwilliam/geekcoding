class Solution {
    public int[] dailyTemperatures(int[] T) {
        int length = T.length;
        int[] tem = new int[length];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < length; i++) {

            while (!stack.isEmpty() && T[stack.peek()] < T[i]) {
                int diff = i - stack.peek();
                tem[stack.pop()] = diff;
            }

            stack.push(i);
        }

        return tem;
    }
}