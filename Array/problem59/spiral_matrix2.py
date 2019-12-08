'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
'''
class Solution:
    def generateMatrix(self, n):
        arr = [[0] * n for i in range(n)]
        turn = 0  # 0 Switch between Horizontal and Vertical
        val, loopCount = 0, 0
        move = 1  # 1 for Right,Down and -1 for Left and Up
        level = 0  # While Going Inside
        i, j = 0, -1

        while val < n * n:

            if turn == 0:
                # Move Left,Right Till the End or the Next Element if Full
                while j + move < n - level and arr[i][j + move] == 0:
                    val += 1
                    j += move
                    arr[i][j] = val

                turn = 1
            else:
                # Move Down,UP Till the End or the next Element if Full
                while i + move < n - level and arr[i + move][j] == 0:
                    val += 1
                    i += move
                    arr[i][j] = val

                turn = 0
            loopCount += 1
            move = -move if loopCount % 2 == 0 else move
            level += 1 if loopCount % 4 == 0 else 0
        print(arr)
        return arr
'''
        if n == 1:
            return [1]
        else:
            max_index = n * n
            answer = [1] * (n * n)
            index_answer = 0
            down_x = n - 1
            right_y = n - 1
            left_y = 0
            up_x = 0
            index_x = 0
            index_y = 0
            while index_answer != max_index:
                if index_x == up_x and index_y == left_y:
                    while index_y != right_y:
                        answer[index_answer] = 4 * index_x + index_y + 1
                        index_y += 1
                        index_answer += 1
                        if index_answer == max_index:
                            print(answer)
                            return answer
                    answer[index_answer] = 4 * index_x + index_y + 1
                    index_x += 1
                    up_x += 1
                    print(answer)

                    continue
                elif index_x == up_x and index_y == right_y:
                    while index_x != down_x:
                        answer[index_answer] = 4 * index_x + index_y + 1
                        index_x += 1
                        index_answer += 1
                        if index_answer == max_index:
                            print(answer)
                            return answer
                    answer[index_answer] = 4 * index_x + index_y + 1
                    right_y -= 1
                    index_y -= 1
                    return
                    continue
                elif index_x == down_x and index_y == right_y:
                    while index_y != left_y:
                        answer[index_answer] = 4 * index_x + index_y + 1
                        index_y -= 1
                        index_answer += 1
                        if index_answer == max_index:
                            print(answer)
                            return answer
                    answer[index_answer] = 4 * index_x + index_y + 1
                    down_x -= 1
                    index_x -= 1
                    continue
                elif index_x == down_x and index_y == left_y:
                    while index_x != up_x:
                        answer[index_answer] = 4 * index_x + index_y + 1
                        index_x -= 1
                        index_answer += 1
                        if index_answer == max_index:
                            print(answer)
                            return answer
                    answer[index_answer] = 4 * index_x + index_y + 1
                    left_y += 1
                    index_y += 1
                    continue
            print(answer)
            return answer
'''




nums1 = [0, 2, 1, 2, 0, 1]
function = Solution()
function.generateMatrix(4)