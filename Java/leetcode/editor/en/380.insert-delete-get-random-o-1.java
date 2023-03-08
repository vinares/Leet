package leetcode.editor.en;

import java.util.ArrayList;
import java.util.HashMap;

/*
 * @lc app=leetcode id=380 lang=java
 *
 * [380] Insert Delete GetRandom O(1)
 */

// @lc code=start
class RandomizedSet {
    ArrayList<Integer> data;
    HashMap<Integer, Integer> ht;
    java.util.Random rand = new java.util.Random();

    public RandomizedSet() {
        data = new ArrayList<Integer> ();
        ht = new HashMap<Integer,Integer>();
    }
    
    public boolean insert(int val) {
        if (ht.containsKey(val)) return false;
        ht.put(val, data.size());
        data.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if (!ht.containsKey(val)) return false;
        int val_index = ht.get(val);
        if (val_index < data.size()-1){
            int last_val = data.get(data.size()-1);
            ht.put(last_val, val_index);
            data.set(val_index, last_val);
        }
        ht.remove(val);
        data.remove(data.size()-1);
        return true;
    }
    
    public int getRandom() {
        return data.get(rand.nextInt(data.size()));
    }
}

/**
 * Your leetcode.editor.en.RandomizedSet object will be instantiated and called as such:
 * leetcode.editor.en.RandomizedSet obj = new leetcode.editor.en.RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
// @lc code=end

