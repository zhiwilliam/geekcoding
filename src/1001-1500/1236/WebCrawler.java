
public class WebCrawler {
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
        Set<String> visited = new HashSet<>();
        Queue<String> queue = new ArrayDeque<>();
        
        String[] tem = startUrl.split("/");
        String hostname = tem[2];

        queue.offer(startUrl);
        visited.add(startUrl);
        
        while(!queue.isEmpty()){
            
            for(int size = queue.size(); size > 0; size--){
                String current = queue.poll();
                
                for(String url : htmlParser.getUrls(current)){
                    if(!visited.contains(url) && url.split("/")[2].equals(hostname)){
                        visited.add(url);
                        queue.offer(url);
                    }
                        
                }
            }
        }
        return new ArrayList<>(visited);
    }
}