class Solution {
    public int largestComponentSize(int[] A) {
		int mx = 0;
		for (int i : A) {
			mx = Math.max(i, mx);
		}
		p = new int[mx + 1];
		for (int i = 1; i <= mx; ++i) {
			p[i] = i;
		}
		for (int i : A) {
			for (int j = (int) Math.sqrt(i); j>=2; j--) {
				if (i > j &&  i % j == 0) {
					add(i, j);
					if (j != i/j) {
						add(i, i/j);
					}
				}
			}
		}
		
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		int res = 0;
		for (int i : A) {
			int j = get(i);
			if (!map.containsKey(j)) {
				map.put(j, 1);
			} else {
				map.put(j, map.get(j) + 1);
			}
			res = Math.max(res, map.get(j));
		}
		return res;
	}
    
    int[] p;

	int get(int x) {
		return p[x] == x ? x : (p[x] = get(p[x]));
	}

	void add(int x, int y) {
		p[get(x)] = p[get(y)];
	}
}