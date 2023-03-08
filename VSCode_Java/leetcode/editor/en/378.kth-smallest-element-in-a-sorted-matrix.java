package leetcode.editor.en;

import java.util.PriorityQueue;

/*
 * @lc app=leetcode id=378 lang=java
 *
 * [378] Kth Smallest Element in a Sorted Matrix
 */

// @lc code=start

class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length;
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>(new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return a[0] - b[0];
            }
        });
        for (int i=0; i<m; i++){
            pq.offer(new int[] {matrix[i][0], i, 0});
        }
        for (int i=0; i<k-1; i++){
            int[] cur = pq.poll();
            if(cur[2] != n-1)
                pq.offer(new int[] {matrix[cur[1]][cur[2]+1], cur[1], cur[2]+1});
        }
        return pq.peek()[0];
    }
}
// @lc code=end
