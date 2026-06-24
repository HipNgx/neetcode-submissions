class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = []
        count_ = 0
        def Island(hang : int, cot : int) -> int :
            nonlocal count_
            if hang < 0 or hang >= len(grid) or cot < 0 or cot >= len(grid[hang]):
                return
            if grid[hang][cot] == 0 or [hang, cot] in visited :
                return
            visited.append([hang,cot])
            huong = [[hang,cot+1],[hang+1,cot],[hang-1,cot],[hang,cot-1]]
            for row, col in huong :
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == 0 :
                    count_ += 1
                elif [row, col] not in visited :
                    Island(row, col) 
        n = len(grid)
        for hang in range(n) :
            for cot in range (len(grid[hang])) :
                if grid[hang][cot] == 1 :
                    Island(hang,cot)
                    break
        return count_