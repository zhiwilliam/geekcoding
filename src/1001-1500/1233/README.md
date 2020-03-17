#1233. Remove Sub-Folders from the Filesystem
Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

If a folder[i] is located within another folder[j], it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

```python
Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".
Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
 

Constraints:

1 <= folder.length <= 4 * 10^4
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'
folder[i] always starts with character '/'
Each folder name is unique.
```

#Source Code
```java
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
```