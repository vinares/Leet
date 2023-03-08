import java.util.*;

class Solution{
    private static final int d[] = {0, 1, 0, -1, 0};

    private boolean dfs(int i, int j, int x, int y, int[][] grid, List<List<Integer>> island){
        int m = grid.length;
        int n = grid[0].length;

        if(x<0 || x>=m || y<0 || y>=n || grid[i][j] <= 0)
            return false;
        grid[x][y]=-1;
        island.add(Arrays.asList(x-i, y-j));
        for (int k=0; k<4; k++){
            dfs(i, j, x+d[k], y+d[k+1], grid, island);
        }
        return true;
    }

    public int numDistinctIslands(int[][] grid){
        if (grid==null || grid[0].length==0)
            return 0;
        int m = grid.length;
        int n = grid[0].length;
        Set<List<List<Integer>>> distinct_islands = new HashSet<>();

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                List<List<Integer>> island = new ArrayList<>();
                if(dfs(i, j, i, j, grid, island)){
                    distinct_islands.add(island);
                }
            }
        }
        return distinct_islands.size();
    }

    public static void main(String[] args) {
        int[][] grid = { {1,1,0,1,1}, {1,0,0,0,0},{0,0,0,0,1},{1,1,0,1,1}};
        Solution solution = new Solution();
        System.out.println(solution.numDistinctIslands(grid));
    }
}

