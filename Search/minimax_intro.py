tree = {
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "C" : ["F", "G"],
}

values = {
    "D": 3,
    "E": 5,
    "F": 2,
    "G": 9
}

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

def print_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):

            curr = board[row][col]

            if curr == None :
               print("\t-\t",end="")

            elif curr == 'X':
                print("\tX\t",end="")

            else : print("\tO\t",end="")
        print("")

def actions(board):

    arr = []

    for row in range(len(board)):

        for col in range(len(board[row])):
        
            if board[row][col] == None : 
                arr.append((row,col))

    return arr


def player(board): 
    x = 0
    o = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X' : x += 1
            elif board[i][j] == 'O' : o += 1

    if x <= o : return 'X'
    else : return 'O'


def isLeaf(ch):
    return not ch in tree

def score(ch):
    return values[ch]


def result(board, action):

    new_board = [row[:] for row in board]
    
    row,col = action 
    new_board[row][col] = player(board)
        
    return new_board
        
def winner(board):
    
    for row in range(len(board)):
        curr_player = board[row][0]
        flag = True
        for col in range(1,len(board[row])):
            if board[row][col] != curr_player or board[row][col]== None: 
                flag = False
                break
        if flag :
            return curr_player
        

    for col in range(len(board[0])):
        curr_player = board[0][col]
        flag = True
        for row in range(1,len(board)):
            if board[row][col] != curr_player or board[row][col]== None : 
                flag = False
                break
        if flag :
            return curr_player
        
    curr_player = board[0][0]
    flag = True
    for row in range(1,len(board)):
        col = row
        if board[row][col] != curr_player or board[row][col]== None : 
            flag = False
            break

    if flag : return curr_player

    curr_player = board[0][2]
    flag = True
    for row in range(1,len(board)):
        col = len(board) - row - 1
        if board[row][col] != curr_player or board[row][col]== None : 
            flag = False
            break

    if flag : return curr_player
        
        
    return None


def terminal(board):

    if winner(board) != None or len(actions(board)) == 0:
        return True
     
    return False

def utility(board):
    
    # considering that terminal(board) == True
    curr_winner = winner(board)

    if curr_winner == 'X':
        return 1
    elif curr_winner == 'O':
        return -1
    return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    
    else :
        maxx = float('-inf')
        for action in actions(board):
            new_board = result(board,action)
            maxx = max(maxx,min_value(new_board))
        return maxx;

def min_value(board):
    if terminal(board):
        return utility(board)
    
    else :
        minn = float('inf')
        for action in actions(board):
            new_board = result(board,action)
            minn = min(minn,max_value(new_board))
        return minn;


def minimax(board):
    
    if terminal(board):
        return None
    
    best_action = None       

    if player(board) == "X":

        curr = -2;
        for action in actions(board):

            value = min_value(result(board,action))

            if curr < value :
                best_action = action
                curr = value


    else:
        curr = 2;
        for action in actions(board):

            value = max_value(result(board,action))

            if curr > value :
                best_action = action
                curr = value
            

    return best_action    
    

# ans_num, ans_state = minimax("A",True)
# print(ans_num)
# print(ans_state)
# print("\t")

# print_board(board)
# # print(p(board))
# print()
# # actions(board)
# # result(board,actions(board))
# print("WINNER : ",winner(board))

while not terminal(board):

    curr = player(board)

    if(curr == 'X'):
        print("HUMAN TURN : ----")
    
    else :
        print("AI PLAYS : ----")
        


    if curr == 'X':
        print_board(board)
        print("")
        row = int(input("Enter the row : "))
        col = int(input("Enter the column : "))

        while True:
            if(row >= 0 and row < 3 and col >= 0 and col < 3):
                break 
            else :
                print("Please, give valid row and column number !!!")
                row = int(input("Enter the row : "))
                col = int(input("Enter the column : "))

        board = result(board,(row,col))

    else :


        best_action = minimax(board)
        print(f"AI chose: {best_action}")
        board = result(board,best_action)
        # print_board(board)
        

    print("")




win = winner(board)
if win == 'X':
    print("HUMAN WINS!!!!")
elif win == 'O':
    print("AI WINS!!!!")
else :
    print("DRAW !!!!")

