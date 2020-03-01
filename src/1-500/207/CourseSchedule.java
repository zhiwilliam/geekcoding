class Solution {
    //Topological BSF
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (numCourses <= 0 || prerequisites == null || prerequisites.length == 0) {
            return true;
        }
        boolean[][] graph = new boolean[numCourses][numCourses];
        int[] indegree = new int[numCourses];
        for (int[] requi : prerequisites) {
            graph[requi[1]][requi[0]] = true;
            indegree[requi[0]]++;

        }
        Queue<Integer> course = new LinkedList<>();
        for (int i = 0; i < indegree.length; i++) {
            if (indegree[i] == 0) {
                course.offer(i);
            }
        }
        int count = 0;
        while(!course.isEmpty()) {
            int cur = course.poll();
            count++;
            for (int i = 0; i < graph[cur].length; i++) {
                if (graph[cur][i]) {
                    if (--indegree[i] == 0) {
                        course.offer(i);
                    }
                }
            }
        }
        return count == numCourses;
    }

}