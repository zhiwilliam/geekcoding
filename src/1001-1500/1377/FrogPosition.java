class Solution {
    public double frogPosition(int n, int[][] edges, int t, int target) {
        List<List<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < n + 1; i++)
            graph.add(i, new ArrayList<>());

        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        double[] probability = new double[n + 1];
        boolean[] visited = new boolean[n + 1];
        probability[1] = 1.0;

        return bfs(graph, visited, 1, t, target, probability);
    }

    private double bfs(List<List<Integer>> graph, boolean[] visited, int start, int t, int target,
            double[] probability) {

        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        visited[start] = true;
        double probablity = 1;

        while (!queue.isEmpty() && t-- > 0) {
            int size = queue.size();

            for (int i = 0; i < size; i++) {

                int v = queue.poll();
                int curSize = 0;

                for (int u : graph.get(v)) {
                    if (!visited[u])
                        curSize++;
                }

                for (int u : graph.get(v)) {

                    if (!visited[u]) {
                        probability[u] = probability[v] / curSize;
                        visited[u] = true;
                        queue.add(u);
                    }
                }

                if (curSize > 0)
                    probability[v] = 0;
            }
        }

        return probability[target];
    }
}