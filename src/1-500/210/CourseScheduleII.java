class Solution {
    //BST topoligical sort seems easier
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        boolean[][] graph = new boolean[numCourses][numCourses];
        int[] indegree = new int[numCourses];
        for (int[] requi : prerequisites) {
            graph[requi[1]][requi[0]] = true;
            indegree[requi[0]]++;
        }
        List<Integer> ans = new ArrayList<>();
        Queue<Integer> courses = new LinkedList<>();
        for (int i = 0; i < indegree.length; i++) {
            if (indegree[i] == 0) {
                courses.offer(i);
            }
        }
        while(!courses.isEmpty()) {
            int cur = courses.poll();
            ans.add(cur);
            for (int i = 0; i < graph[cur].length; i++) {
                if (graph[cur][i]) {
                    if (--indegree[i] == 0) {
                        courses.offer(i);
                    }
                }
            }
        }
        int[] res = ans.stream().mapToInt(i ->i).toArray();
        return res.length == numCourses ? res : new int[0];
    }

}