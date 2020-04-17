class Solution {
    private int longest = 0;
    private int startNode = 0;
    public int treeDiameter(int[][] edges) {
        if (edges == null || edges.length == 0) {
            return 0;
        }
        Map<Integer, List<Integer>> graph = getGraph(edges);
        Set<Integer> visited = new HashSet<>();
        dfs(0, graph, visited, 0);
        dfs(this.startNode, graph, visited, 0);
        return this.longest;
    }

    private void dfs(int cur, Map<Integer, List<Integer>> map, Set<Integer> visited, int depth) {
        if (visited.add(cur)) {
            if (depth > longest) {
                this.startNode = cur;
                this.longest = depth;
            }
            for (int next : map.get(cur)) {
                dfs(next, map, visited, depth + 1);
            }
            visited.remove(cur);
        }
        return;
    }

    private Map<Integer, List<Integer>> getGraph(int[][] edges) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int[] edge : edges) {
            List<Integer> listU = map.getOrDefault(edge[0], new ArrayList<>());
            listU.add(edge[1]);
            map.put(edge[0], listU);
            List<Integer> listV = map.getOrDefault(edge[1], new ArrayList<>());
            listV.add(edge[0]);
            map.put(edge[1], listV);
        }
        return map;
    }
}