package OA;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;


//LC 819
public class MostCommonWord {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> set = new HashSet<>(Arrays.asList(banned));
        
        String[] para = paragraph.toLowerCase().split("\\W+");
        //String[] words = paragraph.toLowerCase().split("[ !?',;.]+");
        Map<String, Integer> map = new HashMap<>();
        
        for(String str : para){
            if(!set.contains(str))
                map.put(str, map.getOrDefault(str, 0) + 1);
        }
        
        int max = 0;
        String tem = null;
        for(Map.Entry<String, Integer> entry : map.entrySet()){
            if(entry.getValue() > max){
                max = entry.getValue();
                tem = entry.getKey();
            }
        }
        
        return tem;
    }
}