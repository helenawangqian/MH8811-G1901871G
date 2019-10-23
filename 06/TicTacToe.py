#!/usr/bin/env python
# coding: utf-8

# In[4]:


def TicTacToe(board):
    value_0 = ' O '
    value_1 = ' X '
    value_2 = '   '
    n = len(board)
    counter = 0
    for j in range(n):
        actual_board = ''
        counter += 1
        for i in range(n):
            if i < n-1:
                if board[j][i]==0:
                    actual_board += value_0 + '|'
                elif board[j][i]==1:
                    actual_board += value_1 + '|'
                elif board[j][i]==2:
                    actual_board += value_2 + '|'
            else:
                if board[j][i]==0:
                    actual_board += value_0 
                elif board[j][i]==1:
                    actual_board += value_1 
                elif board[j][i]==2:
                    actual_board += value_2 
        print(actual_board)
        if counter < n:
            dash ='-'*(3*len(board)) + '-'*(len(board)-1)
            print(dash)
            
            
            

TicTacToe([[0,1,1,1,2,0],[2,1,1,1,1,1],[0,1,2,1,0,2],[2,1,0,0,0,1],[1,2,1,2,1,0],[1,1,1,2,2,2]])

print('\n')

TicTacToe([[0,1,2],[2,0,0],[1,1,2]])


# In[ ]:




