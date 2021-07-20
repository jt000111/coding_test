board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]


answer = 0
box = []

for i in range(len(moves)):
    for j in range(len(board)):
        if board[j][moves[i]-1] == 0:
            pass
        else:
            box.append(board[j][moves[i]-1])
            board[j][moves[i]-1] = 0
            break




    for k in range(len(box)-1):
        if box[k] == box[k+1]:
            answer += 2
            del box[k]
            del box[k]
            break
        

print(box)