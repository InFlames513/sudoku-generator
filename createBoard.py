import numpy as np
import random
board = np.full((9,9), -1)

def check():
  for r in range(9):
    unique_arr_row = np.bincount(board[r][board[r] != -1])
    if (unique_arr_row > 1).any():
      return False
    
  for c in range(9):
    column = board[:, c]
    unique_arr_col = np.bincount(column[column != -1])
    if (unique_arr_col > 1).any():
      return False

  box_arr = [[] for _ in range(9)]

  for b in range(9):
    for bc in range(3):
      for br in range(3):
        if b == 0 or b == 3 or b == 7:
          box_arr[b].append(board[int(b/3)*3+br][bc])
        elif b == 1 or b == 4 or b == 8:
          box_arr[b].append(board[int(b/3)*3+br][bc+3])
        else:
          box_arr[b].append(board[int(b/3)*3+br][bc+6])

  for num in range(9):
    unique_arr_box = np.bincount(np.array(box_arr[num])[np.array(box_arr[num]) != -1])
    if (unique_arr_box > 1).any():
          return False
  return True


def create_board():
  for col in range(9): # Fill in the columns
    while True:
      for row in range(9): # Fill in the rows
        l = 0
        while True: # Check the rows
          l = l+1
          num = random.randint(1, 9) # Generate a random number between 0 and 9
          board[col][row] = num
          if check():
            break
          elif l == 25: 
            board[col] = [-1 for _ in range(9)]
            l = 0
      if len(board[col][board[col] != -1]) == 9:
        break

  return board
