class LRUCache {
    int cap;
    LinkedHashMap<Integer,Integer> cache;
    public LRUCache(int capacity) {
        cap=capacity;
        cache=new LinkedHashMap<>(cap,0.75f,true);
    }
    public int get(int key) {
        if(cache.containsKey(key))return cache.get(key);
        return  -1;
    }
    public void put(int key, int value) {
        cache.put(key,value);
        if(cache.size()>cap){
            int lkey=cache.keySet().iterator().next();
            cache.remove(lkey);
    }}
}