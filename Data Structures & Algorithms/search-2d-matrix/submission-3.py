class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)) :
            if target > matrix[i][-1] :
                continue
            if matrix[i][0] <= target <= matrix[i][-1] :
                l, r = 0, len(matrix[i]) - 1
                while l <= r :
                    mid = (l + r) // 2
                    cur = matrix[i][mid]
                    if cur == target :
                        return True
                    elif cur > target :
                        r = mid-1
                    else :
                        l = mid + 1 
        return False

