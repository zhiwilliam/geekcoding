class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        if (cpdomains == null || cpdomains.length == 0) {
            return new ArrayList<>();
        }
        List<String> ans = new ArrayList<>();
        Map<String, Integer> count = new HashMap<>();
        for (String str : cpdomains) {
            String[] array = str.split("\\s");
            int curCount = Integer.parseInt(array[0]);
            String key = array[1];
            for (int i = key.length() - 1; i >= 0; i--) {
                if (key.charAt(i) == '.') {
                    String subKey = key.substring(i + 1, key.length());
                    int newCount = count.getOrDefault(subKey, 0) + curCount;
                    count.put(subKey, newCount);
                }
            }
            int newCount = count.getOrDefault(key, 0) + curCount;
            count.put(key, newCount);
        }
        for (Map.Entry<String, Integer> entry : count.entrySet()) {
            ans.add(String.join(" ", String.valueOf(entry.getValue()), entry.getKey()));
        }
        return ans;
    }
}