class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, List<String>> graph = new HashMap<>();
        List<String> list = new ArrayList<>();

        // build the graph
        for (int i = 0; i < tickets.size(); i++) {

            String from = tickets.get(i).get(0);
            String to = tickets.get(i).get(1);

            if (graph.containsKey(from)) {
                graph.get(from).add(to);
            } else {
                graph.put(from, new ArrayList<>());
                graph.get(from).add(to);
            }
        }

        for (List<String> str : graph.values()) {
            Collections.sort(str);
        }

        dfs(graph, list, "JFK");

        return list;
    }

    private void dfs(Map<String, List<String>> graph, List<String> list, String next) {

        while (graph.containsKey(next) && !graph.get(next).isEmpty()) {
            String nextStop = graph.get(next).remove(0);
            dfs(graph, list, nextStop);
        }

        list.add(0, next);
    }
}