class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for j in range(len(matrix)):
            i=0
            upper=len(matrix[0])-1
            
            while i<=upper:
                mid=(i+upper)//2
                print(j,mid)
                if matrix[j][mid]<target:
                    i=mid+1
                elif matrix[j][mid]>target:
                    upper=mid-1
                else:
                    return True
        return False