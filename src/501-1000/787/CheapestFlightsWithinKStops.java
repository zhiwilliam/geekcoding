class Solution {
  int total = Integer.MAX_VALUE;

  public int findCheapestPrice(
    int n,
    int[][] flights,
    int src,
    int dst,
    int K
  ) {
    Map<Integer, List<int[]>> map = new HashMap<>();
    Set<Integer> visited = new HashSet<>();

    for (int[] flight : flights) {
      if (map.containsKey(flight[0])) map
        .get(flight[0])
        .add(new int[] { flight[1], flight[2] }); else {
        map.put(flight[0], new ArrayList<>());
        map.get(flight[0]).add(new int[] { flight[1], flight[2] });
      }
    }

    dfs(map, visited, src, dst, K, 0);
    return total == Integer.MAX_VALUE ? -1 : total;
  }

  private void dfs(
    Map<Integer, List<int[]>> map,
    Set<Integer> visited,
    int src,
    int dst,
    int K,
    int cost
  ) {
    if (src == dst) {
      total = cost;
      return;
    }

    if (K < 0 || visited.contains(src) || !map.containsKey(src)) return;

    visited.add(src);

    for (int[] current : map.get(src)) {
      if (current[1] + cost > total) continue;
      dfs(map, visited, current[0], dst, K - 1, cost + current[1]);
    }

    visited.remove(src);
  }
}
