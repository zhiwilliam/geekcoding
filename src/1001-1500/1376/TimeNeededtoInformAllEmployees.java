class Solution {
    //we can have another bottom-up recuresion to do this
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

//Bottom-up recuresion

class Solution {
    public int numOfMinutes(final int n, final int headID, final int[] manager, final int[] informTime) {
        final Map<Integer, List<Integer>> graph = new HashMap<>();
        int total = 0;
        for (int i = 0; i < manager.length; i++) {
            int j = manager[i];
            if (!graph.containsKey(j))
                graph.put(j, new ArrayList<>());
            graph.get(j).add(i);
        }
        return dfs(graph, informTime, headID);
    }

    private int dfs(final Map<Integer, List<Integer>> graph, final int[] informTime, final int cur) {
        int max = 0;
        if (!graph.containsKey(cur))
            return max;
        for (int i = 0; i < graph.get(cur).size(); i++)
            max = Math.max(max, dfs(graph, informTime, graph.get(cur).get(i)));
        return max + informTime[cur];
    }
}