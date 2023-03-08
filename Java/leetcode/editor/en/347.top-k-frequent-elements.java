package leetcode.editor.en;

import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

/*
 * @lc app=leetcode id=347 lang=java
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> occurrences = new HashMap<Integer, Integer>();
        for (int num : nums) {
            occurrences.put(num, occurrences.getOrDefault(num, 0) + 1);
        }

        List<Integer>[] list = new List[nums.length+1];
        for(int key : occurrences.keySet()){
            int i = occurrences.get(key);
            if (list[i] == null)
                list[i] = new ArrayList();
            list[i].add(key);
        }
        int[] ans = new int[k];
        int j = 0;
        for(int i = list.length-1; i>=0 && j<k; i--){
            if (list[i]==null) continue;
            for (int p=0; p<list[i].size() && j<k; p++){
                ans[j] = list[i].get(p);
                j++;
            }
        }
        return ans;
        
    }
}
// @lc code=end
