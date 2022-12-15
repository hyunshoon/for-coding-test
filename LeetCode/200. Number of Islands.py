class Solution(object):
    #상하좌우

    def BFS(self, r,c, grid, visited):
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        m = len(grid)
        n = len(grid[0])
        queue = deque()

        queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for i in range(4):
                cr = r + dr[i]
                cc = c + dc[i]
                if cr < 0 or cr > m-1 or cc<0 or cc> n-1:
                    continue
                if grid[cr][cc] == '0' or visited[cr][cc] == True:
                    continue
                visited[cr][cc] = True
                queue.append((cr,cc))



    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        answer = 0
        visited = [ [False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False and grid[i][j] == '1':
                    self.BFS(i,j, grid, visited)
                    answer +=1
        return answer
