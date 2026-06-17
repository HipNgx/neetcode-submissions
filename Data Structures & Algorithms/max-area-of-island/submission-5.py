class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = []
        max_value  = 0
        def AreaOfIsland(hang : int, cot : int) -> int :
            if hang < 0 or hang >= len(grid) or cot < 0 or cot >= len(grid[hang]):
                return 0
            if grid[hang][cot] == 0 or [hang, cot] in visited :
                return 0
            visited.append([hang, cot])
            return 1 + AreaOfIsland(hang, cot + 1) + AreaOfIsland(hang, cot-1)+ AreaOfIsland(hang+1, cot) + AreaOfIsland(hang-1, cot)
        for hang in range(len(grid)) :
            for cot in range(len(grid[hang])) :
                if grid[hang][cot] == 1 and [hang, cot] not in visited :
                    max_value = max(AreaOfIsland(hang, cot), max_value)
        return max_value



        