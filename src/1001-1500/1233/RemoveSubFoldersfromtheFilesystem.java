class Solution {
    public List<String> removeSubfolders(String[] folder) {
        List<String> ans = new ArrayList<>();
        if (folder == null || folder.length == 0) {
            return ans;
        }
        Folder root = new Folder("");
        Arrays.sort(folder, (a, b) -> a.length() - b.length());
        for (String str : folder) {
            String[] subs = str.split("/");
            boolean isExist = false;
            Folder newRoot = root;
            for (int i = 1; i < subs.length; i++) {
                String sub = subs[i];
                if (!isExist && !newRoot.isLeaf()) {
                    newRoot.addSub(sub);
                    newRoot = newRoot.getSub(sub);
                } else {
                    isExist = true;
                }
            }
            if (!isExist) {
                newRoot.setLeaf();
                ans.add(str);
            }
        }
        return ans;
    }
}

class Folder {
    String val;
    Map<String, Folder> subs;
    boolean leaf;
    public Folder(String val) {
        this.val = val;
        this.subs = new HashMap();
        this.leaf = false;
    }

    public boolean addSub(String sub) {
        if (this.subs.containsKey(sub)) {
            return false;
        }
        this.subs.put(sub, new Folder(sub));
        return true;
    }

    public Folder getSub(String sub) {
        return this.subs.get(sub);
    }

    public void setLeaf() {
        this.leaf = true;
    }

    public boolean isLeaf() {
        return this.leaf;
    }
}