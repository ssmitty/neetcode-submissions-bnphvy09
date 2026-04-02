class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            r=len(matrix[0])-1
            l=0
            while r>=l:
                mid=r+l//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]<target:
                    l=mid+1
                else:
                    r=mid-1

        return False