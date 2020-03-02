class Solution {
    
    private boolean[][] visited;
    
    private int postOrder(int r, int c, int[][] picture) {
        if (picture[r][c] == 0) {
            return 0;
        }
        
        if (visited[r][c]) {
            return 0;
        }
        
        this.visited[r][c] = true;
        
        int up = 0, down = 0, left = 0, right = 0;
        if (r - 1 >= 0 && picture[r][c] == picture[r - 1][c] && !visited[r - 1][c]) {
            up = postOrder(r - 1, c, picture);
        }
        
        if (r  + 1 < picture.length && picture[r][c] == picture[r + 1][c] && !visited[r + 1][c]) {
            down = postOrder(r + 1, c, picture);
        }
        
        if (c - 1 >= 0 && picture[r][c] == picture[r][c - 1] && !visited[r][c - 1]) {
            left = postOrder(r, c - 1, picture);
        }
        
        if (c + 1 < picture[0].length && picture[r][c] == picture[r][c + 1] && !visited[r][c + 1]) {
            right = postOrder(r, c + 1, picture);
        }
    
        return up + down + left + right + 1;
    }

    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        visited = new boolean[m][n];

        for (int r = 0 ; r < m ; r++) {
            for (int c = 0 ; c < n ; c++) {
                int size = this.postOrder(r, c, picture);           
                if (size > 0) {
                    numberOfArea += 1;

                    if (size > maxSizeOfOneArea) {
                        maxSizeOfOneArea = size;
                    }
                }
            }
        }
        
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}