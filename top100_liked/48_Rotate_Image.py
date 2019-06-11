from leeyzer import solution, timeit, Solution, make_tree, TreeNode

# @Date: 2019/6/11
# @Author: *** 
# @description:


class Q48_Rotate_Image(Solution):
    @timeit
    @solution
    def Q48_Rotate_Image1(self, matrix):
        """
        先沿正对角线反转，再沿中轴反转
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        m = n // 2
        for i in range(n):
            for j in range(m):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][2 * m - j]
                matrix[i][2 * m - j] = tmp
        # 实现了原地修改，这里是为了输出return
        return matrix
    
    @timeit
    @solution
    def Q48_Rotate_Image2(self, matrix):
    
        pass    
    

def main():
    q = Q48_Rotate_Image()
    q.add_args([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ])
    # q.add_args()
    q.test()


if __name__ == "__main__":
    main()
