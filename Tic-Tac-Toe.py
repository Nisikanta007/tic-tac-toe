board = {
    1:"1", 2:"2", 3:"3",
    4:"4", 5:"5", 6:"6",
    7:"7", 8:"8", 9:"9"
}

for i in range(9):
    
    print()
    print(board[1], "|", board[2], "|", board[3])
    print("----------")
    print(board[4], "|", board[5], "|", board[6])
    print("----------")
    print(board[7], "|", board[8], "|", board[9])
    
    
    pos = int(input("Enter position: "))
    
    if i % 2 == 0:
        board[pos] = "x"
    else:
        board[pos] = "0"
        
        
    if (board[1] == board[2] == board[3] or
        board[4] == board[5] == board[6] or
        board[7] == board[8] == board[9] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[3] == board[6] == board[9] or
        board[1] == board[5] == board[9] or
        board[3] == board[5] == board[7] ):
        
        if i % 2 == 0:
            print("player: 1 wins.")
        else:
            print("player: 2 wins.")
            
        break
else:
     print("match is draw.")
        