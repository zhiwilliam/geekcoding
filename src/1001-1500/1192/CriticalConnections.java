
public class CriticalConnections {
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {

        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0; i < n; i++)
            graph.add(new ArrayList<>());
        
        for(int i = 0; i < connections.size(); i++){
            int from = connections.get(i).get(0);
            int to = connections.get(i).get(1);
            
            graph.get(from).add(to);
            graph.get(to).add(from);
        }
        
        
        //int n, id;
        int id = 0;
        int[] low = new int[n];
        int[] dfn = new int[n];
        boolean[] visited = new boolean[n];
        List<List<Integer>> result = new ArrayList<>();
        
        for(int i = 0; i < n; i++){
            if(!visited[i])
                dfs(i , -1, result, low, dfn, visited, id, graph);
        }
        
        return result;
    }
    
    private void dfs(int at, int parent, List<List<Integer>> result, int[] low, int[] dfn, boolean[] visited, int id, List<List<Integer>> graph){
        visited[at] = true;
        low[at] = dfn[at] = id++;
        
        for(int to : graph.get(at)){
            if(to == parent)
                continue;
            
            if(!visited[to]){
                dfs(to, at, result, low, dfn, visited, id, graph);
                low[at] = Math.min(low[at], low[to]);
                
                if(dfn[at] < low[to]){
                    result.add(Arrays.asList(at, to));
                }
            } else {
                low[at] = Math.min(low[at], low[to]);
            }
        }
    }
}