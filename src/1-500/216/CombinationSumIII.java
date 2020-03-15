class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> ans = new ArrayList<>();
        if (k == 0 || n <= 0) {
            return ans;
        }
        buildList(ans, new ArrayList<>(), 1, n, k);
        return ans;
    }

    private void buildList(List<List<Integer>> ans, List<Integer> list, int index, int n, int k) {
        if (list.size() >= k && n > 0) {
            return;
        }
        if (n < 0 && list.size() <= k) {
            return;
        }
        if (n == 0 && list.size() == k) {
            ans.add(new ArrayList<>(list));
            return;
        }
        for (int i = index; i <= 9; i++) {
            list.add(i);
            buildList(ans, list, i + 1, n - i, k);
            list.remove(list.size() - 1);
        }
        return;
    }
}