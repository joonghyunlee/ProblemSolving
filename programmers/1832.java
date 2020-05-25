import java.util.Arrays;
import java.util.Queue;
import java.util.LinkedList;

class Solution {
    int MOD = 20170805;
    private int getCount(int[][] cityMap, int[][] count, int row, int col) {
        if (row == 0 && col == 0) {
            return 1;
        }

        int c = 0;
        int tR = row;
        while (tR - 1 >= 0) {
            if (cityMap[tR - 1][col] == 0) {
                c += count[tR][col + 1];
                break;
            } else if (cityMap[tR - 1][col] == 1) {
                break;
            } else if (cityMap[tR - 1][col] == 2) {
                tR -= 1;
            }
        }

        int tC = col;
        while (tC - 1 >= 0) {
            if (cityMap[row][tC - 1] == 0) {
                c += count[row + 1][tC];
                break;
            } else if (cityMap[row][tC - 1] == 1) {
                break;
            } else if (cityMap[row][tC - 1] == 2) {
                tC -= 1;
            }
        }

        return c % MOD;
    }

    public int solution(int m, int n, int[][] cityMap) {
        int[][] count = new int[m + 1][n + 1];
        for (int[] row : count) {
            Arrays.fill(row, 0);
        }

        for (int row = 0 ; row < m ; row++) {
            for (int col = 0 ; col < n ; col++) {
                count[row + 1][col + 1] = this.getCount(cityMap, count, row, col);
            }
        }

        return count[m][n];
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] cityMap1 = {
            {0, 0, 0},
            {0, 0, 0},
            {0, 0, 0}
        };
        System.out.println(s.solution2(3, 3, cityMap1));
        
        int[][] cityMap2 = {
            {0, 2, 0, 0, 0, 2},
            {0, 0, 2, 0, 1, 0},
            {1, 0, 0, 2, 2, 0}
        };
        System.out.println(s.solution2(3, 6, cityMap2));
    }
}