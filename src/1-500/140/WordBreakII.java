class Solution {
    //bottom up recursion with memorization
    public List<String> wordBreak(String s, List<String> wordDict) {
        return dfs(s, wordDict, new HashMap<String, List<String>>());
    }

    private List<String> dfs(String s, List<String> wordDict, Map<String, List<String>> memo) {
        if (memo.containsKey(s)) {
            return memo.get(s);
        }
        List<String> list = new ArrayList<>();
        if (s.length() == 0) {
            list.add("");
            return list;
        }
        for (String str : wordDict) {
            if (s.startsWith(str)) {
                List<String> subList = dfs(s.substring(str.length()), wordDict, memo);
                if (!subList.isEmpty()) {
                    for (String eachStr : subList) {
                        list.add(str + (eachStr.isEmpty() ? "" : " " + eachStr));
                    }
                }

            }
        }
        memo.put(s, list);
        return list;
    }
}