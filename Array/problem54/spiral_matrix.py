'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
'''
class Solution:
    def spiralOrder(self, matrix):
        def getFirstNeighbor(matrix, last_position, position, visited):

            last_x, last_y = last_position
            c_x, c_y = position

            delta_x = c_x - last_x
            delta_y = c_y - last_y

            # We have moved from the left
            if delta_y > 0 or (delta_x == 0 and delta_y == 0):
                neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            elif delta_y < 0:
                neighbors = [[0, -1], [-1, 0], [0, 1], [1, 0]]
            elif delta_x > 0:
                neighbors = [[1, 0], [0, -1], [-1, 0], [0, 1]]
            elif delta_x < 0:
                neighbors = [[-1, 0], [0, 1], [1, 0], [0, -1]]

            for n_x, n_y in neighbors:
                # Verify position is valid
                if c_x + n_x < len(matrix) and c_x + n_x >= 0 and c_y + n_y >= 0 and c_y + n_y < len(matrix[0]) and (
                c_x + n_x, c_y + n_y) not in visited:
                    return (c_x + n_x, c_y + n_y)

        def dfs(matrix, last_position, position, visited, output):
            if not position:
                return

            x, y = position
            if (x, y) not in visited:
                visited.add((x, y))
                output.append(matrix[x][y])
                dfs(matrix, position, getFirstNeighbor(matrix, last_position, position, visited), visited, output)

        output = []
        visited = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                dfs(matrix, [row, col], [row, col], visited, output)

        return output
        '''
        down_x = len(matrix) - 1
        right_y = len(matrix[1]) - 1
        left_y = 0
        up_x = 0
        answer = [1] * (down_x*right_y)
        index_ans = 0
        index_x = 0
        index_y = 0
        print(down_x)
        print(right_y)
        print(answer)
        while down_x != up_x or right_y != left_y:
            if index_x == up_x and index_y == left_y:
                while index_y != right_y:
                    answer[index_ans] = matrix[index_x][index_y]
                    print(answer[index_ans])
                    index_y += 1
                    index_ans += 1

                index_x += 1
                up_x += 1
                index_y -= 1
                print("*")
                print(answer[0:4])
                print(index_x)
                print(up_x)
                print(index_y)
                print(right_y)
                print(down_x)
            elif index_x == up_x and index_y == right_y:
                while index_x != down_x:
                    answer[index_ans] = matrix[index_x][index_y]
                    print(answer[index_ans])
                    index_x += 1
                    index_ans += 1
                right_y -= 1
                index_y -= 1
                print("*")
                print(answer[4:8])
                print(index_x)
                print(up_x)
                print(index_y)
                print(right_y)
            elif index_x == down_x and index_y == right_y:
                while index_y != left_y:
                    answer[index_ans] = matrix[index_x][index_y]
                    index_y -= 1
                    index_ans += 1
                down_x -= 1
                index_x -= 1
            elif index_x == down_x and index_y == left_y:
                while index_x != up_x:
                    answer[index_ans] = matrix[index_x][index_y]
                    index_x -= 1
                    index_ans += 1
                left_y += 1
                index_y += 1
        print(answer)
        return answer
        '''


nums1 = [[3, 4, 0, 2], [1, 2, 3, 4]]
function = Solution()
function.spiralOrder(nums1)