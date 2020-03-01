class MedianFinder {
  private Queue<Integer> maxHeap;
  private Queue<Integer> minHeap;

  /** initialize your data structure here. */
  public MedianFinder() {
    // max heap keep smaller half
    maxHeap = new PriorityQueue<>((a, b) -> (b - a));
    // min heap keep lager half
    minHeap = new PriorityQueue<>((a, b) -> (a - b));
  }

  public void addNum(int num) {
    if (maxHeap.size() == minHeap.size()) {
      minHeap.offer(num);
      maxHeap.offer(minHeap.poll());
    } else {
      maxHeap.offer(num);
      minHeap.offer(maxHeap.poll());
    }
  }

  public double findMedian() {
    if (maxHeap.size() == minHeap.size()) return (
      (minHeap.peek() + maxHeap.peek()) / 2.0
    );

    return maxHeap.peek();
  }
}
/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder(); obj.addNum(num); double param_2 =
 * obj.findMedian();
 */
