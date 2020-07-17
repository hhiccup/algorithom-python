
#################### 排列、组合、子集 及其升级版 可直接查看下面网址 #########################

https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/ 


###################### 1 全排列 ###################

class Solution: #try1  仿照上一个做过的 组合题，也是回溯法
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        n = len(nums)
        res = []

        def recur(nums, pre):
            if len(pre) == n:
             #   pre.append(nums[0])
                res.append(pre[:])
                return
            for i in range(len(nums)):
                tmp = nums.pop(i)
                pre.append(tmp)
                recur(nums, pre)
                pre.pop()
                nums.insert(i, tmp)
        recur(nums, [])
        return res



##################### 2 组合 #############################

class Solution: #参考回朔法题解
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n<=0 or k <= 0 or n < k: # 先把不符合条件的情况去掉
            return []
        result = []
        
        def recur(start, n, k, tmpList):
            if len(tmpList) == k:
                print(tmpList)
                result.append(tmpList[:]) # ！！！注意：要在列表append（列表），需要用[:]!!
                return # !!!记得return 才能终结！！！
            for i in range(start, n+1):
                tmpList.append(i)
                recur(i + 1, n, k, tmpList)
                tmpList.pop()
        recur(1, n, k, [])
        return result
        
#################### 3 子集 ####################

'''
class Solution: #视频讲的 迭代/回溯法   不是回溯算法的固定模板！！不推荐
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def recur(nums, index, tmp):
            if index == len(nums):
                result.append(tmp[:])# += tmp
                return
            #不包含第index个数
            recur(nums, index + 1, tmp)
            #包含第index个数
            tmp.append(nums[index])
            recur(nums, index + 1, tmp)
            #(回溯)撤销本层添加的元素（tmp临时结果会在最底层被使用，这里删除）
            tmp.pop()
        recur(nums, 0, [])
        return result
'''
class Solution: #test1题解 回溯算法固定模板！！
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def backTrack(idx, tmp):
            #自己不需要加 （或者法二：外面再加一个for循环，用不同k去限制下探层数）
            result.append(tmp[:])
            for i in range(idx, n):
                tmp.append(nums[i])
                backTrack(i + 1, tmp) #注意是i + 1 ，不是idx！！！
                tmp.pop()
                # 注意！！！三句其实可以合并为： backTrack(idx + 1, n, tmp + [nums[i]]) !!! 且此时的tmp已经是新的列表了，可以用append（tmp）去添加
        backTrack(0, [])
        return result


##################### 4 电话号码的字母组合 ################


class Solution: #test1 看懂题解思路后 回溯法
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: # 注意！！！ 每个题最好还是先进行特判，最后运行成功之后再优化掉吧。不然可能会出意外错
            return []
        nums = [',', ',', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        n = len(digits)
        numbers = ''.join(digits) # ['2', '4']
        result = []

        def backtrack(level, tmp):
            if level == n:
                result.append(tmp)
                return
            curNums = nums[int(numbers[level])]
            for i in curNums:
               # tmp += i
                backtrack(level + 1, tmp + i)   
               # tmp.pop() #字符串怎么去掉最后一位？？用切片！！
        backtrack(0, '')
        return result
        


###################### 5 N皇后 ###################

'''
class Solution: # 回溯模板 题解
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for _ in range(n)] #初始化二维棋盘
        print(board)
        res=[]

        def backtrack(board,row):
        #     if 满足条件:
        #         res.append(路径)
        #         return
            if row==len(board):
                tmp_list=[] #二维变一维添加到res中
                for e_row in board:
                    tmp=''.join(e_row)
                    tmp_list.append(tmp)
                res.append(tmp_list)
                return
        #     for 选择 in 选择列表:
        #         做选择
        #         backtrack(路径,选择列表)
        #         撤销选择
            for col in range(len(board[0])):
                if not isValid(board,row,col):
                    # print(isValid(board,row,col))
                    continue
                board[row][col]='Q'
                # print(board)
                backtrack(board,row+1)
                board[row][col]='.'
    

        def isValid(board,row,col):
            n=len(board)
            # 检查列是否有皇后互相冲突
            for i in range(n):
                if board[i][col]=='Q':
                    return False
            # 检查右上方是否有皇后互相冲突
            r_row,r_col=row,col
            while r_row>0 and r_col<n-1:
                r_row-=1
                r_col+=1
                if board[r_row][r_col]=='Q':
                    return False
            # 检查左上方是否有皇后互相冲突
            l_row,l_col=row,col
            while l_row>0 and l_col>0:
                l_row-=1
                l_col-=1
                if board[l_row][l_col]=='Q':
                    return False
            return True


        backtrack(board,0)
        return res

class Solution: #官方题解
    def solveNQueens(self, n: int) -> List[List[str]]:
        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
        
        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1
        
        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0
        
        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)
        
        def backtrack(row = 0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)
        
        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output
'''
 
class Solution: #test1 回溯模板  写了25min以上。。。
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0: return []
        board = [['.'] * n for _ in range(n)]
        result = []

        def backtrack(board, cur_row):
            if cur_row == n:
                #将该解法从列表转换为str（二维转成一维）
                # for i in board:
                #     tmp.append(''.join(i)) 
                tmp = [''.join(i) for i in board]  #上面两行可简化为此             
                result.append(tmp)
            for cur_col in range(n):
                if is_valid(board, cur_row, cur_col): #判断不会冲突时
                    board[cur_row][cur_col] = 'Q'  #注意！！！是复制！！！不是 == 
                    backtrack(board, cur_row + 1)#准备在下一行放Q
                    board[cur_row][cur_col] = '.'
        
        def is_valid(board, cur_row, cur_col):
            #先判断正上方有无Q
            for j in range(cur_row):
                if board[j][cur_col] == 'Q':
                    return False
            #判断左上对角
            tmprow, tmpcol = cur_row, cur_col
            while tmprow > 0 and tmpcol > 0:
                tmprow -= 1
                tmpcol -= 1
                if board[tmprow][tmpcol] == 'Q':
                    return False
            
            #判断you上对角
            tmprow, tmpcol = cur_row, cur_col
            while tmprow > 0 and tmpcol < n - 1:
                tmprow -= 1
                tmpcol += 1
                if board[tmprow][tmpcol] == 'Q':
                    return False
            return True

        backtrack(board, 0)
        return result

        

