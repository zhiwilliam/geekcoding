class Solution {
    public String rankTeams(String[] votes) {
        if (votes.length == 1)
            return votes[0];

        Map<Character, int[]> map = new HashMap<>();
        int len = votes[0].length();

        for (int i = 0; i < votes.length; i++) {
            for (int pos = 0; pos < len; pos++) {
                char ch = votes[i].charAt(pos);
                if (map.containsKey(ch)) {
                    map.get(ch)[pos]++;
                } else {
                    map.put(ch, new int[len]);
                    map.get(ch)[pos]++;
                }
            }
        }

        List<Character> list = new ArrayList<>(map.keySet());
        Collections.sort(list, (a, b) -> {
            for (int i = 0; i < len; i++) {
                if (map.get(a)[i] != map.get(b)[i]) {
                    return map.get(b)[i] - map.get(a)[i];
                }
            }

            return a - b;
        });

        StringBuilder sb = new StringBuilder();
        for (Character ch : list) {
            sb.append(ch);
        }

        return sb.toString();
    }
}
