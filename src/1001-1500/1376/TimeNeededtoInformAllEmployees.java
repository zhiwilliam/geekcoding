class Solution {
    //build a tree using map
    private int ans = 0;
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        if (n == 1) {
            return 0;
        }
        Map<Integer, Node> map = new HashMap<>();
        int headId = 0;
        for (int i = 0; i < n; i++) {
            Node node = map.getOrDefault(i, new Node(i));
            map.put(i, node);
            if (manager[i] != -1) {
                Node boss = map.getOrDefault(manager[i], new Node(manager[i]));
                map.put(manager[i], boss);
                boss.sub.add(i);
            } else {
                headId = i;
            }
        }
        findTime(map, headId, 0, informTime);
        return ans;
    }

    private void findTime(Map<Integer, Node> map, int root, int curTime, int[] informTime) {
        if (map.get(root).sub.isEmpty()) {
            this.ans = Math.max(ans, curTime);
            return;
        }
        for (int next : map.get(root).sub) {
            findTime(map, next, curTime + informTime[root], informTime);
        }
        return;
    }
}

class Node {
    int id;
    int mins;
    List<Integer> sub;

    public Node(int id) {
        this.sub = new ArrayList<>();
    }
}