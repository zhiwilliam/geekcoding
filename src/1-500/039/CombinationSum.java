class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        if (candidates == null || candidates.length == 0) {
            return ans;
        }
        Arrays.sort(candidates);
        buildList(ans, new ArrayList<Integer>(), 0, candidates, target);
        return ans;
    }

    private void buildList(List<List<Integer>> ans, List<Integer> list, int index, int[] candidates, int target) {
        if (target == 0) {
            ans.add(new ArrayList<>(list));
            return;
        }
        if (target < 0) {
            return;
        }
        for (int i = index; i < candidates.length; i++) {
            if (target - candidates[i] < 0) {
                break;
            }
            list.add(candidates[i]);
            buildList(ans, list, i, candidates, target - candidates[i]);
            list.remove(list.size() - 1);
        }
        return;
    }
}