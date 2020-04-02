class MyCalendar {
    
    //TreeMap<Integer, Integer> calendar;
    TreeSet<int[]> books;

    public MyCalendar() {
        //calendar = new TreeMap();
        books = new TreeSet<int[]>((int[] a, int[] b) -> a[0] - b[0]);
    }
    
    public boolean book(int s, int e) {
        int[] book = new int[] { s, e }, floor = books.floor(book), ceiling = books.ceiling(book);
        if (floor != null && s < floor[1]) return false; // (s, e) start within floor
        if (ceiling != null && ceiling[0] < e) return false; // ceiling start within (s, e)
        books.add(book);
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */