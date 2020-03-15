class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        if (candidates == null || candidates.length == 0) {
            return ans;
        }
        Arrays.sort(candidates);
        buildList(ans, new ArrayList<>(), 0, target, candidates);
        return ans;
    }

    private void buildList(List<List<Integer>> ans, List<Integer> list, int index, int target, int[] candidates) {
        if (target < 0) {
            return;
        }
        if (target == 0) {
            ans.add(new ArrayList<>(list));
            return;
        }
        for (int i = index; i < candidates.length; i++) {
            if (i > index && candidates[i] == candidates[i- 1]) {
                continue;
            }
            if (target - candidates[i] < 0) {
                break;
            }
            list.add(candidates[i]);
            buildList(ans, list, i + 1, target - candidates[i], candidates);
            list.remove(list.size() - 1);
        }
        return;
    }
}