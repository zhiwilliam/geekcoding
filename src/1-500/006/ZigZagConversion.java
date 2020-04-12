class Solution {
    public String convert(String s, int numRows) {
		if (s==null || s.isEmpty() || numRows <= 1 || s.length() <= numRows) return s;
		
		int len = s.length();
		int lenCycle = 2 * numRows - 2;
		StringBuilder res = new StringBuilder();

		for (int i=0; i< numRows; i++) {
			for (int j=0; j+i<len; j+=lenCycle) {
				res.append(s.charAt(j+i));
				if (i!=0 && i!=numRows-1 && j+lenCycle-i<len) {
					res.append(s.charAt(j+lenCycle-i));
				}
			}			
		}
		
		return res.toString();
	}
}