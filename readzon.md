大致在pycharm -> editor -> live templates,具体百度
搭配readme后添加内容及参数示例如下:

from leeyzer import solution, timeit, Solution, make_tree, TreeNode

# @Date: $date$
# @Author: *** 
# @description:

class Q$name$(Solution):
    @solution
    def Q$name$1(self):
        
        pass
    
    
    @timeit
    @solution
    def Q$name$2(self):
    
        pass    
    

def main():
    q = Q$name$()
    q.add_args()
    q.add_args()
    q.test()

if __name__ == "__main__":
    main()
