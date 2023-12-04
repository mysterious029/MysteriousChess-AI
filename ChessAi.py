#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
np.__version__
import math
import random
import chess


# In[ ]:


class chess_m:
  def __init__(self):
      self.board = chess.Board()
      self.final = False
      self.row_count = 8
      self.column_count = 8
      self.action_size = 224
      self.p2 = [[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7]]
      self.p1 = [[6,0],[6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7],[7,0],[7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7]]
      
  def get_initial_board(self):
      return self.board.copy()
    
  def get_revB_move(self,move):
      num = ['1','2','3','4','5','6','7','8']
      ch = np.array(['a','b','c','d','e','f','g','h']) 
      r_old = 8-int(move[1])
      r_new = 8-int(move[3])
      c_old = np.where(ch == move[0])
      c_new = np.where(ch == move[2])
      return r_old,int(c_old[0]),r_new,int(c_new[0])
    
  def rc_to_value(self,r_old,c_old,r_new,c_new):
      action = 0
      type = 0
      player = 0
      for i in range(16):
        if r_old == self.p1[i][0] and c_old == self.p1[i][1]:
            type = i
            player = 1
            break
        if r_old == self.p2[i][0] and c_old == self.p2[i][1]:
            type = i
            player = -1
            break
      if player == 1:
        if type < 8:
            action = type*4
            if(c_old == c_new):
                if r_old - r_new == 1:
                    action += 1
                else:
                    action += 2
            else:
                if c_new < c_old :
                    action += 3
                else:
                    action += 4
        elif type == 8 or type == 15:
            if type == 8:
                action = 32
            else:
                action = 60
            if(c_old == c_new):
                if r_new < r_old:
                    action += (r_old - r_new)
                else:
                    action += (7 + r_new - r_old)
            else:
                if c_new < c_old:
                    action += (14 + c_old - c_new)
                else:
                    action += (21 + c_new - c_old)
        elif type == 9 or type == 14:
            if type == 9:
                action = 88
            else:
                action = 96
            if r_new - r_old == -2:
                if(c_new < c_old):
                    action += 1
                else:
                    action += 2
            elif r_new - r_old == 2:
                if(c_new < c_old):
                    action += 3
                else:
                    action += 4
            elif r_new - r_old == -1:
                if(c_new < c_old):
                    action += 5
                else:
                    action += 6
            else:
                if(c_new < c_old):
                    action += 7
                else:
                    action += 8
        elif type == 10 or type == 13:
            if type == 10:
                action = 104
            else:
                action = 132
            if r_new < r_old and c_new > c_old:
                action += (c_new - c_old)
            elif r_new > r_old and c_new < c_old:
                action += (7 + c_old - c_new)
            elif r_new < r_old and c_new < c_old:
                action += (14 + c_old - c_new)
            else:
                action += (21 + c_new - c_old)
        elif type == 11:
            action = 160
            if r_new != r_old and c_new != c_old:
                if r_new < r_old and c_new > c_old:
                    action += (c_new - c_old)
                elif r_new > r_old and c_new < c_old:
                    action += (7 + c_old - c_new)
                elif r_new < r_old and c_new < c_old:
                    action += (14 + c_old - c_new)
                else:
                    action += (21 + c_new - c_old)
            else:
                action += 28
                if(c_old == c_new):
                    if r_new < r_old:
                        action += (r_old - r_new)
                    else:
                        action += (7 + r_new - r_old)
                else:
                    if c_new < c_old:
                        action += (14 + c_old - c_new)
                    else:
                        action += (21 + c_new - c_old)
        else:
            action = 216
            if r_new != r_old and c_new != c_old:
                if r_new < r_old and c_new > c_old:
                    action += 1
                elif r_new > r_old and c_new < c_old:
                    action += 2
                elif r_new < r_old and c_new < c_old:
                    action += 3
                else:
                    action += 4
            else:
                action += 4
                if(c_old == c_new):
                    if r_new < r_old:
                        action += 1
                    else:
                        action += 2
                else:
                    if c_new < c_old:
                        action += 3
                    else:
                        action += 4
      else:
        if type < 8:
            action = type*4
            if(c_old == c_new):
                if r_new - r_old == 1:
                    action += 1
                else:
                    action += 2
            else:
                if c_new < c_old :
                    action += 3
                else:
                    action += 4
        elif type == 8 or type == 15:
            if type == 8:
                action = 32
            else:
                action = 60
            if(c_old == c_new):
                if r_old < r_new:
                    action += (r_new - r_old)
                else:
                    action += (7 + r_old - r_new)
            else:
                if c_new < c_old:
                    action += (14 + c_old - c_new)
                else:
                    action += (21 + c_new - c_old)
        elif type == 9 or type == 14:
            if type == 9:
                action = 88
            else:
                action = 96
            if r_old - r_new == -2:
                if(c_new < c_old):
                    action += 1
                else:
                    action += 2
            elif r_old - r_new == 2:
                if(c_new < c_old):
                    action += 3
                else:
                    action += 4
            elif r_old - r_new == -1:
                if(c_new < c_old):
                    action += 5
                else:
                    action += 6
            else:
                if(c_new < c_old):
                    action += 7
                else:
                    action += 8
        elif type == 10 or type == 13:
            if type == 10:
                action = 104
            else:
                action = 132
            if r_old > r_new and c_new > c_old:
                action += (c_new - c_old)
            elif r_new < r_old and c_new < c_old:
                action += (7 + c_old - c_new)
            elif r_new > r_old and c_new < c_old:
                action += (14 + c_old - c_new)
            else:
                action += (21 + c_new - c_old)
        elif type == 11:
            action = 160
            if r_new != r_old and c_new != c_old:
                if r_new > r_old and c_new > c_old:
                    action += (c_new - c_old)
                elif r_new < r_old and c_new < c_old:
                    action += (7 + c_old - c_new)
                elif r_new > r_old and c_new < c_old:
                    action += (14 + c_old - c_new)
                else:
                    action += (21 + c_new - c_old)
            else:
                action += 28
                if(c_old == c_new):
                    if r_old < r_new:
                        action += (r_new - r_old)
                    else:
                        action += (7 + r_old - r_new)
                else:
                    if c_new < c_old:
                        action += (14 + c_old - c_new)
                    else:
                        action += (21 + c_new - c_old)
        else:
            action = 216
            if r_new != r_old and c_new != c_old:
                if r_new > r_old and c_new > c_old:
                    action += 1
                elif r_new < r_old and c_new < c_old:
                    action += 2
                elif r_new > r_old and c_new < c_old:
                    action += 3
                else:
                    action += 4
            else:
                action += 4
                if(c_old == c_new):
                    if r_old < r_new:
                        action += 1
                    else:
                        action += 2
                else:
                    if c_new < c_old:
                        action += 3
                    else:
                        action += 4
      return action

  def move_to_action(self,move):
        a,b,c,d = self.get_revB_move(move)
        action = self.rc_to_value(a,b,c,d)
        return action
      
  def get_initial_state(self):
      a = [[-5,-4,-3,-8,-10,-3,-4,-5],
      [-1,-1,-1,-1,-1,-1,-1,-1],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [1,1,1,1,1,1,1,1],
      [5,4,3,8,10,3,4,5]]
      a = np.array(a)
      return a

  def get_next_state(self, state, action, player):
      r_old = 0
      c_old = 0
      r_new = 0
      c_new = 0
      piece_value = 0
      if action <= 32:
          if action <= 4:
                if player == 1:
                    r_old , c_old = self.p1[0]
                else:
                    r_old , c_old = self.p2[0]
          elif action > 4 and action <= 8:
                if player == 1:
                    r_old , c_old = self.p1[1]
                else:
                    r_old , c_old = self.p2[1]
          elif action > 8 and action <= 12:
                if player == 1:
                    r_old , c_old = self.p1[2]
                else:
                    r_old , c_old = self.p2[2]
          elif action > 12 and action <= 16:
                if player == 1:
                    r_old , c_old = self.p1[3]
                else:
                    r_old , c_old = self.p2[3]
          elif action > 16 and action <= 20:
                if player == 1:
                    r_old , c_old = self.p1[4]
                else:
                    r_old , c_old = self.p2[4]
          elif action > 20 and action <= 24:
                if player == 1:
                    r_old , c_old = self.p1[5]
                else:
                    r_old , c_old = self.p2[5]
          elif action > 24 and action <= 28:
                if player == 1:
                    r_old , c_old = self.p1[6]
                else:
                    r_old , c_old = self.p2[6]
          else:
                if player == 1:
                    r_old , c_old = self.p1[7]
                else:
                    r_old , c_old = self.p2[7]
          piece_value = player*1
          if action %4 == 1:
                if player == 1:
                    r_new = r_old - 1
                    c_new = c_old
                else:
                    r_new = r_old + 1
                    c_new = c_old
          elif action %4 == 2:
                if player == 1:
                    r_new = r_old - 2
                    c_new = c_old
                else:
                    r_new = r_old + 2
                    c_new = c_old
          elif action %4 == 3:
                if player == 1:
                    r_new = r_old - 1
                    c_new = c_old - 1
                else:
                    r_new = r_old + 1
                    c_new = c_old - 1
          else:
                if player == 1:
                    r_new = r_old - 1
                    c_new = c_old + 1
                else:
                    r_new = r_old + 1
                    c_new = c_old + 1
            
      elif action > 32 and action <= 88:
          if action <= 60:
                if player == 1:
                    r_old , c_old = self.p1[8]
                else:
                    r_old , c_old = self.p2[8]
          else:
                if player == 1:
                    r_old , c_old = self.p1[15]
                else:
                    r_old , c_old = self.p2[15]
          piece_value = 5*player
          action = action - 32
          if action > 28:
                action = action - 28
          if action <= 7:
                if player == 1:
                    r_new = r_old - ((action-1)%7 + 1)
                    c_new = c_old
                else:
                    r_new = r_old + ((action-1)%7 + 1)
                    c_new = c_old
          elif action > 7 and action <= 14:
                if player == 1:
                    r_new = r_old + ((action-1)%7 + 1)
                    c_new = c_old
                else:
                    r_new = r_old - ((action-1)%7 + 1)
                    c_new = c_old
          elif action > 14 and action <= 21:
                if player == 1:
                    r_new = r_old
                    c_new = c_old - ((action-1)%7 + 1)
                else:
                    r_new = r_old
                    c_new = c_old - ((action-1)%7 + 1)
          else:
                if player == 1:
                    r_new = r_old
                    c_new = c_old + ((action-1)%7 + 1)
                else:
                    r_new = r_old
                    c_new = c_old + ((action-1)%7 + 1)
      elif action > 88 and action <= 104:
          if action <= 96:
                if player == 1:
                    r_old , c_old = self.p1[9]
                else:
                    r_old , c_old = self.p2[9]
          else:
                if player == 1:
                    r_old , c_old = self.p1[14]
                else:
                    r_old , c_old = self.p2[14]
          piece_value = 3*player
          action = action - 88
          if action > 8:
                action = action - 8
          if action == 1:
                if player == 1:
                    r_new = r_old - 2
                    c_new = c_old - 1
                else:
                    r_new = r_old + 2
                    c_new = c_old - 1
          elif action == 2:
                if player == 1:
                    r_new = r_old - 2
                    c_new = c_old + 1
                else:
                    r_new = r_old + 2
                    c_new = c_old + 1
          elif action == 3:
                if player == 1:
                    r_new = r_old + 2
                    c_new = c_old - 1
                else:
                    r_new = r_old - 2
                    c_new = c_old - 1
          elif action == 4:
                if player == 1:
                    r_new = r_old + 2
                    c_new = c_old + 1
                else:
                    r_new = r_old - 2
                    c_new = c_old + 1
          elif action == 5:
                if player == 1:
                    r_new = r_old - 1
                    c_new = c_old - 2
                else:
                    r_new = r_old + 1
                    c_new = c_old - 2
          elif action == 6:
                if player == 1:
                    r_new = r_old - 1
                    c_new = c_old + 2
                else:
                    r_new = r_old + 1
                    c_new = c_old + 2
          elif action == 7:
                if player == 1:
                    r_new = r_old + 1
                    c_new = c_old - 2
                else:
                    r_new = r_old - 1
                    c_new = c_old - 2
          else:
                if player == 1:
                    r_new = r_old + 1
                    c_new = c_old + 2
                else:
                    r_new = r_old - 1
                    c_new = c_old + 2
      elif action > 104 and action <= 160:
          if action <= 132:
                if player == 1:
                    r_old , c_old = self.p1[10]
                else:
                    r_old , c_old = self.p2[10]
          else:
                if player == 1:
                    r_old , c_old = self.p1[13]
                else:
                    r_old , c_old = self.p2[13]
          piece_value = 4*player
          action = action - 104
          if action > 28:
                action = action - 28
          if action <= 7:
                if player == 1:
                    r_new = r_old - ((action-1)%7 + 1)
                    c_new = c_old + ((action-1)%7 + 1)
                else:
                    r_new = r_old + ((action-1)%7 + 1)
                    c_new = c_old + ((action-1)%7 + 1)
          elif action > 7 and action <= 14:
                if player == 1:
                    r_new = r_old + ((action-1)%7 + 1)
                    c_new = c_old - ((action-1)%7 + 1)
                else:
                    r_new = r_old - ((action-1)%7 + 1)
                    c_new = c_old - ((action-1)%7 + 1)
          elif action > 14 and action <= 21:
                if player == 1:
                    r_new = r_old - ((action-1)%7 + 1)
                    c_new = c_old - ((action-1)%7 + 1)
                else:
                    r_new = r_old + ((action-1)%7 + 1)
                    c_new = c_old - ((action-1)%7 + 1)
          else:
                if player == 1:
                    r_new = r_old + ((action-1)%7 + 1) 
                    c_new = c_old + ((action-1)%7 + 1)
                else:
                    r_new = r_old - ((action-1)%7 + 1)
                    c_new = c_old + ((action-1)%7 + 1)
      elif action > 160 and action <= 216:
          if player == 1:
                r_old , c_old = self.p1[11]
          else:
                r_old , c_old = self.p2[11]
          piece_value = 8*player
          action = action - 160
          if action <= 7:
                if player == 1:
                    r_new = r_old - ((action-1)%7 + 1)
                    c_new = c_old + ((action-1)%7 + 1)
                else:
                    r_new = r_old + ((action-1)%7 + 1)
                    c_new = c_old + ((action-1)%7 + 1)
          elif action > 7 and action <= 14:
                if player == 1:
                    r_new = r_old + ((action-1)%7 + 1)
                    c_new = c_old - ((action-1)%7 + 1)
                else:
                    r_new = r_old - ((action-1)%7 + 1)
                    c_new = c_old - ((action-1)%7 + 1)
          elif action > 14 and action <= 21:
                if player == 1:
                    r_new = r_old - ((action-1)%7 + 1)
                    c_new = c_old - ((action-1)%7 + 1)
                else:
                    r_new = r_old + ((action-1)%7 + 1)
                    c_new = c_old - ((action-1)%7 + 1)
          elif action > 21 and action <= 28:
                if player == 1:
                    r_new = r_old + ((action-1)%7 + 1)
                    c_new = c_old + ((action-1)%7 + 1)
                else:
                    r_new = r_old - ((action-1)%7 + 1)
                    c_new = c_old + ((action-1)%7 + 1)
          elif action > 28 and action <= 35:
                if player == 1:
                    r_new = r_old - ((action-1)%7 + 1)
                    c_new = c_old
                else:
                    r_new = r_old + ((action-1)%7 + 1)
                    c_new = c_old
          elif action > 35 and action <= 42:
                if player == 1:
                    r_new = r_old + ((action-1)%7 + 1)
                    c_new = c_old
                else:
                    r_new = r_old - ((action-1)%7 + 1)
                    c_new = c_old
          elif action > 42 and action <= 49:
                if player == 1:
                    r_new = r_old
                    c_new = c_old - ((action-1)%7 + 1)
                else:
                    r_new = r_old
                    c_new = c_old - ((action-1)%7 + 1)
          else:
                if player == 1:
                    r_new = r_old
                    c_new = c_old + ((action-1)%7 + 1)
                else:
                    r_new = r_old
                    c_new = c_old + ((action-1)%7 + 1)
      else:
          if player == 1:
                r_old , c_old = self.p1[12]
          else:
                r_old , c_old = self.p2[12]
          piece_value = 10*player
          action = action - 216
          if action == 1:
                if player == 1:
                    r_new = r_old - 1
                    c_new = c_old + 1
                else:
                    r_new = r_old + 1
                    c_new = c_old + 1
          elif action == 2:
                if player == 1:
                    r_new = r_old + 1
                    c_new = c_old - 1
                else:
                    r_new = r_old - 1
                    c_new = c_old - 1
          elif action == 3:
                if player == 1:
                    r_new = r_old - 1
                    c_new = c_old - 1
                else:
                    r_new = r_old + 1
                    c_new = c_old - 1
          elif action == 4:
                if player == 1:
                    r_new = r_old + 1
                    c_new = c_old + 1
                else:
                    r_new = r_old - 1
                    c_new = c_old + 1
          elif action == 5:
                if player == 1:
                    r_new = r_old - 1
                    c_new = c_old
                else:
                    r_new = r_old + 1
                    c_new = c_old
          elif action == 6:
                if player == 1:
                    r_new = r_old + 1
                    c_new = c_old
                else:
                    r_new = r_old - 1
                    c_new = c_old
          elif action == 7:
                if player == 1:
                    r_new = r_old 
                    c_new = c_old - 1
                else:
                    r_new = r_old 
                    c_new = c_old - 1
          else:
                if player == 1:
                    r_new = r_old
                    c_new = c_old + 1
                else:
                    r_new = r_old
                    c_new = c_old + 1
      state[r_old,c_old] = 0
      if player == 1:
            for i in range(16):
                if r_old == self.p1[i][0] and c_old == self.p1[i][1]:
                    self.p1[i][0] = r_new
                    self.p1[i][1] = c_new
                    break
            for i in range(16):
                if r_new == self.p2[i][0] and c_new == self.p2[i][1]:
                    if i == 13:
                        self.final == True
                    self.p2[i][0] = -1
                    self.p2[i][1] = -1
                    break
      else:
            for i in range(16):
                if r_old == self.p2[i][0] and c_old == self.p2[i][1]:
                    self.p2[i][0] = r_new
                    self.p2[i][1] = c_new
                    break
            for i in range(16):
                if r_new == self.p1[i][0] and c_new == self.p1[i][1]:
                    if i == 13:
                        self.final == True
                    self.p1[i][0] = -1
                    self.p1[i][1] = -1
                    break
      state[r_new,c_new] = piece_value
      move = self.get_Board_moves(r_old,c_old,r_new,c_new)
      self.board.push_san(move)
      return state

  def get_Board_moves(self,r_old,c_old,r_new,c_new):
      num = ['1','2','3','4','5','6','7','8']
      ch = ['a','b','c','d','e','f','g','h']
      str = ch[c_old]+num[7-r_old]+ch[c_new]+num[(7-r_new)]
      return str

  def get_valid_moves(self, state):
      a = np.zeros(self.action_size + 1)
      l = np.array(list(self.board.legal_moves))
      c = "aaa"
      x = 0
      for i in range(l.size):
        c = str(l[i])
        x = self.move_to_action(c)
        a[x] = 1
      return a

  def get_valid_list(self,state):
        l = np.array(list(self.board.legal_moves))
        b = self.get_valid_moves(state)
        a = np.zeros(l.size)
        k = 0
        for i in range(225):
            if b[i] == 1:
                a[k] = i
                k = k+1
        return a

  def check_win(self, state, action):
      if action == None:
          return False
      
      if self.board.is_checkmate() == True:
          return True
      else:
          return False

  def get_value_and_terminated(self, state, action):
        if self.check_win(state, action):
            return 1, True
        if self.board.is_stalemate() == True:
            return 0, True
        return 0, False
    
  def get_opponent(self, player):
      return -player
  
  def get_opponent_value(self, value):
      return -value
  
  def change_perspective(self, state, player):
      new_state = state.copy()
      for i in range(8):
        for j in range(8):
            new_state[i][j] = state[7-i][j]
      for i in range(16):
        if(self.p1[i][0] != -1):
            self.p1[i][0] = 7 - self.p1[i][0]
      for i in range(16):
        if(self.p2[i][0] != -1):
            self.p2[i][0] = 7 - self.p2[i][0]
      return new_state * player
game = chess_m()
s = game.get_initial_state()
li = game.get_valid_list(s)
print(s)
print(game.board)
print(li)
print("----------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------")
s = game.get_next_state(s,1,1)
li = game.get_valid_list(s)
print(s)
print(game.board)
print(li)
print("----------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------")
s = game.get_next_state(s,1,-1)
li = game.get_valid_list(s)
print(s)
print(game.board)
print(li)
print("----------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------")


# In[ ]:


class Node:
    def __init__(self, game, args, state, parent=None, action_taken=None):
        self.game = game
        self.args = args
        self.state = state
        self.parent = parent
        self.action_taken = action_taken
        
        self.children = []
        self.expandable_moves = game.get_valid_moves(state)
        
        self.visit_count = 0
        self.value_sum = 0
        
    def is_fully_expanded(self):
        return np.sum(self.expandable_moves) == 0 and len(self.children) > 0
    
    def select(self):
        best_child = None
        best_ucb = -np.inf
        
        for child in self.children:
            ucb = self.get_ucb(child)
            if ucb > best_ucb:
                best_child = child
                best_ucb = ucb
                
        return best_child
    
    def get_ucb(self, child):
        q_value = 1 - ((child.value_sum / child.visit_count) + 1) / 2
        return q_value + self.args['C'] * math.sqrt(math.log(self.visit_count) / child.visit_count)
    
    def expand(self):
        action = np.random.choice(np.where(self.expandable_moves == 1)[0])
        self.expandable_moves[action] = 0
        
        child_state = self.state.copy()
        child_state = self.game.get_next_state(child_state, action, 1)
        child_state = self.game.change_perspective(child_state, player=-1)
        print(child_state)
        child = Node(self.game, self.args, child_state, self, action)
        self.children.append(child)
        return child
    
    def simulate(self):
        value, is_terminal = self.game.get_value_and_terminated(self.state, self.action_taken)
        value = self.game.get_opponent_value(value)
        
        if is_terminal:
            return value
        
        rollout_state = self.state.copy()
        rollout_player = 1
        while True:
            valid_moves = self.game.get_valid_moves(rollout_state)
            action = np.random.choice(np.where(valid_moves == 1)[0])
            rollout_state = self.game.get_next_state(rollout_state, action, rollout_player)
            value, is_terminal = self.game.get_value_and_terminated(rollout_state, action)
            if is_terminal:
                if rollout_player == -1:
                    value = self.game.get_opponent_value(value)
                return value    
            
            rollout_player = self.game.get_opponent(rollout_player)
            
    def backpropagate(self, value):
        self.value_sum += value
        self.visit_count += 1
        
        value = self.game.get_opponent_value(value)
        if self.parent is not None:
            self.parent.backpropagate(value)


class MCTS:
    def __init__(self, game, args):
        self.game = game
        self.args = args
        
    def search(self, state):
        root = Node(self.game, self.args, state)
        
        for search in range(self.args['num_searches']):
            node = root
            
            while node.is_fully_expanded():
                node = node.select()
                
            value, is_terminal = self.game.get_value_and_terminated(node.state, node.action_taken)
            value = self.game.get_opponent_value(value)
            
            if not is_terminal:
                node = node.expand()
                value = node.simulate()
                
            node.backpropagate(value)    
            
            
        action_probs = np.zeros(self.game.action_size)
        for child in root.children:
            action_probs[child.action_taken] = child.visit_count
        action_probs /= np.sum(action_probs)
        return action_probs


# In[ ]:


ti = chess_m()
player = 1

args = {
    'C': 1.41,
    'num_searches': 10
}

mcts = MCTS(ti, args)

state = ti.get_initial_state()
while True:
    
    if player == 1:
        print(ti.board)
        valid_moves = ti.get_valid_moves(state)
        print("valid_moves", [i for i in range(ti.action_size) if valid_moves[i] == 1])
        action = int(input(f"{player}:"))
        
        if valid_moves[action] == 0:
            print("action not valid")
            continue
            
    else:
        li = ti.get_valid_list(state)
        action = int(random.choice(li))
    print(action)
    state = ti.get_next_state(state, action, player)
    
    value, is_terminal = ti.get_value_and_terminated(state, action)
    
    if is_terminal:
        print(state)
        if value == 1:
            print(player, "won")
        else:
            print("draw")
        break
        
    player = ti.get_opponent(player)


# In[ ]:




