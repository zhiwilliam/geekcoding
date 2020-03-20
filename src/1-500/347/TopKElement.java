class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i : nums) {
            map.put(i, map.getOrDefault(i, 1) + 1);
        }

        Queue<Integer> queue = new PriorityQueue<>((a, b) -> {
            return map.get(a) - map.get(b);
        });

        for (int i : map.keySet()) {
            queue.offer(i);

            if (queue.size() > k)
                queue.poll();
        }

        List<Integer> list = new ArrayList<>();
        while (!queue.isEmpty()) {
            list.add(0, queue.poll());
        }

        return list;
    }
}