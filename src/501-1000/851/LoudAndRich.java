class Solution {
    private int[] ans;
    private ArrayList<Integer>[] graph;

    public int[] loudAndRich(int[][] richer, int[] quiet) {
        if (quiet == null || quiet.length == 0) {
            return new int[0];
        }
        int N = quiet.length;
        ans = new int[N];
        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<Integer>();
        }
        for (int[] rich : richer) {
            graph[rich[1]].add(rich[0]);
        }
        Arrays.fill(ans, -1); //help update ans;
        for (int i = 0; i < N; i++) {
            dfs(i, ans, graph, quiet);
        }
        return ans;
    }

    private int dfs(int start, int[] ans, ArrayList<Integer>[] graph, int[] quiet) {
        if (ans[start] == -1) {
            ans[start] = start;
            for (int next : graph[start]) {
                int cand = dfs(next, ans, graph, quiet);
                if (quiet[cand] < quiet[ans[start]]) { // compare the quite in sub and current
                    ans[start] = cand;
                }
            }

        }
        return ans[start];
    }
}