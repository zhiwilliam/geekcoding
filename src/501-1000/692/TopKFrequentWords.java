class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        if (words == null || words.length == 0 || k <= 0) {
            return new ArrayList<String>();
        }
        List<String> ans = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        PriorityQueue<Map.Entry<String, Integer>> queue = new PriorityQueue<>((a, b) -> {
            if (a.getValue().compareTo(b.getValue()) == 0) {
                return b.getKey().compareTo(a.getKey());
            }
            return a.getValue().compareTo(b.getValue());
        });
        for (String str : words) {
            int count = map.getOrDefault(str, 0) + 1;
            map.put(str, count);
        }
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            queue.offer(entry);
            if (queue.size() > k) {
                queue.poll();
            }
        }
        while(!queue.isEmpty()) {
            ans.add(0, queue.poll().getKey());
        }
        return ans;
    }
}