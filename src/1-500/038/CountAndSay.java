public class CountAndSay_38 {
    public String countAndSay(int n) {
        if(n == 1) return "1";
        String  s = countAndSay(n-1);
        int count = 0;
        char c = s.charAt(0);
        StringBuilder stringBuilder = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == c){
                count ++;

            }else{
                stringBuilder.append(count).append(c);
                count=1;
                c = s.charAt(i);
            }
            if(i+1>=s.length()){
                stringBuilder.append(count).append(c);
            }
        }
        return stringBuilder.toString();
    }
}