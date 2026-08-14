class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0] * n for _ in range(n)]

        left = 0
        right = n - 1
        top = 0
        bottom = n - 1

        number = 1

        while left <= right and top <= bottom:

            for i in range(left, right + 1):
                arr[top][i] = number
                number += 1

            top += 1

            for i in range(top, bottom + 1):
                arr[i][right] = number
                number += 1

            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    arr[bottom][i] = number
                    number += 1

                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    arr[i][left] = number
                    number += 1

                left += 1

        return arr
        
            
        