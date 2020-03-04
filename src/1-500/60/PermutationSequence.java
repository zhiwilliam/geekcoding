class Solution {
    //factorial method
    public String getPermutation(int n, int k) {
        StringBuilder ans = new StringBuilder();
        List<Integer> list = new ArrayList<>();
        int fac = 1;
        for (int i = 1; i <= n; i++) {
            fac *= i;
            list.add(i);
        }
        for (int i = 0, l = k - 1; i < n; i++) { // index start from 0;
            fac /= (n - i);
            int index = l / fac;
            ans.append(list.get(index));
            list.remove(index);
            l -= index * fac;
        }
        return ans.toString();
    }
}