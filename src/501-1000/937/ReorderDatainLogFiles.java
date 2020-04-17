class Solution {
    public String[] reorderLogFiles(String[] logs) {
        
        
        Arrays.sort(logs, (a, b)->{
            String[] str1 = a.split(" ", 2);
            String[] str2 = b.split(" ", 2);
            
            boolean isdigit1 = Character.isDigit(str1[1].charAt(0));
            boolean isdigit2 = Character.isDigit(str2[1].charAt(0));
            
            if(!isdigit1 && !isdigit2){
                if(str1[1].compareTo(str2[1]) == 0)
                    return str1[0].compareTo(str2[0]);
                else
                    return str1[1].compareTo(str2[1]);
            }
            
            else if(isdigit1 && !isdigit2){
                return 1;
            }
            
            else if(!isdigit1 && isdigit2){
                return -1;
            } 
            
            else {
                return 0;
            }
        });
        
        
        return logs;
    }
}