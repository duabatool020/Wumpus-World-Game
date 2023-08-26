#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
precepts=( "pit", "gold", "empty", "wumpus")
Actions=("Grab gold", "move left", "move right", "move up", "move down", "do nothing","ReturnToStart" )

TopLeftCornerActions=[Actions[2],Actions[4]]
TopActions=[Actions[1],Actions[2],Actions[4]]
TopRightCornerActions=[Actions[1],Actions[4]]
MiddleActions=[Actions[1],Actions[2],Actions[3],Actions[4]]
MiddleLeftActions=[Actions[2],Actions[3],Actions[4]]
MiddleRightActions=[Actions[1],Actions[3],Actions[4]]
BottomLeftActions=[Actions[2],Actions[3]]
BottomActions=[Actions[1],Actions[2],Actions[3]]
BottomRightActions=[Actions[1],Actions[3]]


World=[[precepts[0],precepts[2],precepts[2],precepts[0]],
       [precepts[2],precepts[1],precepts[2],precepts[2]],
       [precepts[2],precepts[2],precepts[3],precepts[0]],
       [precepts[2],precepts[2],precepts[0],precepts[2]]]


class Agent:    
    def __init__(self):
        self.Agentrow=0  
        self.AgentCol=0  
        self.startRow=0  
        self.startCol=0  
        self.NextRow=0   
        self.NextCol=0   
        self.NoOfEmpty=0
        self.NoOfMoves=0 
        self.currentMove=""  
    
    def setValues(self,Agentrow,AgentCol):
        self.Agentrow=Agentrow
        self.AgentCol=AgentCol
   
    def shuffleMatrix(self):  
        random.shuffle(World) 
        
    def DisplayMatrix(self):   
        for i in range(len(World)):
            for j in range(len(World[i])):
                print(World[i][j],end=",  "  )
            print()
       
        
    def SetAgentPosition(self):   
        Agentplaced=False
        for i in range(len(World)):
            for j in range(len(World[i])):
                if World[i][j]=="empty":
                    World[i][j]="Agent"
                    self.startRow=i  
                    self.startCol=j  
                    AgentPlaced=True
                    break
            if AgentPlaced==True:
                break
    
    def GetAgentState(self):    
        for i in range(len(World)):
            for j in range(len(World[i])):
                if World[i][j]=="Agent":
                    self.Agentrow=i
                    self.AgentCol=j
                    
    
    def PossibleMoves(self):  
        if self.Agentrow==0 and self.AgentCol==0:
            return TopLeftCornerActions
        
        elif (self.Agentrow==0 and self.AgentCol==1) or (self.Agentrow==0 and self.AgentCol==2):
            return TopActions
            
        elif self.Agentrow==0 and self.AgentCol==3:
            return TopRightCornerActions
                    
                            
        elif (self.Agentrow==1 and self.AgentCol==0) or (self.Agentrow==2 and self.AgentCol==0):
            return MiddleLeftActions
                    
                            
        elif (self.Agentrow==1 and self.AgentCol==1) or (self.Agentrow==1 and self.AgentCol==2) or (self.Agentrow==2 and self.AgentCol==1) or (self.Agentrow==2 and self.AgentCol==2):
            return MiddleActions
            
        elif (self.Agentrow==1 and self.AgentCol==3) or (self.Agentrow==2 and self.AgentCol==3):
            return MiddleRightActions
            
        elif self.Agentrow==3 and self.AgentCol==0:
            return BottomLeftActions
                    
                            
        elif (self.Agentrow==3 and self.AgentCol==1) or (self.Agentrow==3 and self.AgentCol==2):
            return BottomActions
            
        elif self.Agentrow==3 and self.AgentCol==3:
            return BottomRightActions
        
            
    def GetPrecept(self,move):    
        if move=="move up":
            self.NextRow=self.Agentrow-1
            self.NextCol=self.AgentCol
            return World[self.Agentrow-1][self.AgentCol]
           
        elif move=="move down":
            self.NextRow=self.Agentrow+1
            self.NextCol=self.AgentCol
            return World[self.Agentrow+1][self.AgentCol]
            
        elif move=="move left":
            self.NextRow=self.Agentrow
            self.NextCol=self.AgentCol-1
            return World[self.Agentrow][self.AgentCol-1]
            
        elif move=="move right":
            self.NextRow=self.Agentrow
            self.NextCol=self.AgentCol+1
            return World[self.Agentrow][self.AgentCol+1]
        

    def isgold(self,moves): 
        check=False
        for i in range(len(moves)):
            precept=self.GetPrecept(moves[i])
            if precept=="gold":
                check=True
        if check==True:
            return True
        else:
            return False
                
                    
        
    def isempty(self,moves):  
        check=False
        for i in range(len(moves)):
            precept=self.GetPrecept(moves[i])
            if precept=="empty":

                check=True
        if check==True:
            return True
        else:
            return False
    
    def isStart(self,moves):  
        check=False
        for i in range(len(moves)):
            precept=self.GetPrecept(moves[i])
            if precept=="Start":
                check=True
        if check==True:
            return True
        else:
            return False
        
    def ChooseMovesForGold(self,moves):   #this function takes moves till grabbing the gold
        precept=""
        checkgold=self.isgold(moves)
        if checkgold==True:              #if there is gold then agent will immediately go to that index
            for i in range(len(moves)):
                precept=self.GetPrecept(moves[i])
                if precept=="gold":
                    World[self.Agentrow][self.AgentCol]="empty"
                    World[self.NextRow][self.NextCol]="Agent"
                    self.currentMove=Actions[0]
                    self.NoOfMoves=self.NoOfMoves+1
                    
        else:                              
            checkempty=self.isempty(moves)
            if checkempty==False:   #if there is no empty space means agent cannot move anywhere(do nothing)
                self.currentMove=Actions[5]
            else:                   #if there is empty space move the agent to that empty space and update agent position
                while precept!="empty":
                    random.shuffle(moves)
                    precept=self.GetPrecept(moves[0])
                    if precept=="empty":
                        temp=""
                        temp=World[self.Agentrow][self.AgentCol]
                        World[self.Agentrow][self.AgentCol]=World[self.NextRow][self.NextCol]
                        World[self.NextRow][self.NextCol]=temp
                        self.currentMove=moves[0]
                        self.NoOfMoves=self.NoOfMoves+1
                        break
    
    def ChooseMovesForStart(self,moves): #this function takes moves after grabbing gold till returning to start state
        precept=""
        checkstart=self.isStart(moves)
        if checkstart==True:             #if there is start state of agent adjacent to it, immediately go to that index
            for i in range(len(moves)):
                precept=self.GetPrecept(moves[i])
                if precept=="Start":
                    World[self.Agentrow][self.AgentCol]="empty"
                    World[self.NextRow][self.NextCol]="Agent"
                    self.currentMove=Actions[6]
                    self.NoOfMoves=self.NoOfMoves+1
        
        else:
            checkempty=self.isempty(moves)
            if checkempty==False:         #if there is no empty space means agent cannot move anywhere(do nothing)
                self.currentMove=Actions[5]
            else:                         #if there is empty space move the agent to that empty space and update agent position
                while precept!="empty":
                    random.shuffle(moves)
                    precept=self.GetPrecept(moves[0])
                    if precept=="empty":
                        temp=""
                        temp=World[self.Agentrow][self.AgentCol]
                        World[self.Agentrow][self.AgentCol]=World[self.NextRow][self.NextCol]
                        World[self.NextRow][self.NextCol]=temp
                        self.currentMove=moves[0]
                        self.NoOfMoves=self.NoOfMoves+1
                        break
        
                
    def ReturnToStart(self): #takes moves until agent return to start state
        print()
        print("                  Now return safely To Start State: ")
        print("________________________")
        self.UpdateMatrix()
        self.DisplayMatrix()
        while True:
            self.GetAgentState()
            possibleActions=self.PossibleMoves()
            print("Possible Moves:-------> ",possibleActions)
            self.ChooseMovesForStart(possibleActions)
            print()
            print("Agent has:"  ,self.currentMove,end='   ')
            print("No of Moves taken:" ,self.NoOfMoves)
            print("____________________")
            self.DisplayMatrix()
            print()
            
            if self.currentMove=="ReturnToStart":
                print()
                print("*******Congratulations! YOU WON :)*******")
                break
            
            elif self.currentMove=="do nothing":
                print()
                Print("Agent cannot move in any block---LOOSE :(")
                break
            
            elif self.NoOfMoves>50:
                print()
                print("No of moves exceed----------YOU LOOSE :(")
                break
            
        
    
    def UpdateMatrix(self): #updates the Matrix of Agent after grabbing gold(replace agent start position with start)
        World[self.startRow][self.startCol]="Start"
    
    def StartGame(self):   #thhis function is called in main which is calling every function in it 
        self.shuffleMatrix()
        self.SetAgentPosition()
        self.DisplayMatrix()
        print()
        print("******Game Started********")
        print()
        while True:
            self.GetAgentState()    #sets agent current row and col
            possibleActions=self.PossibleMoves()   #possible actions are returned according to agent row & col
            print("Possible Moves:-------> ",possibleActions)
            self.ChooseMovesForGold(possibleActions)    #function takes moves until gold is grabbed
            print()
            print("Agent has:"  ,self.currentMove,end='   ')
            print("No of Moves taken:" ,self.NoOfMoves)
            print("____________________")
            self.DisplayMatrix()
            print()
            
            if self.currentMove=="Grab gold":  #if gold is grabbed
                self.ReturnToStart()    #then this function is called which takes moves until returned to start state
                break
            
            elif self.currentMove=="do nothing":
                Print("Agent cannot move in any block---LOOSE :(")
                break
            
            elif self.NoOfMoves>50: #if agent take more than 50 moves game will stop
                print()
                print("No of moves exceed----------YOU LOOSE :(")
                break
       
        
        
                
                
#driver Code
obj=Agent()
obj.StartGame()
                    

                    



                        
       
        

            


# In[ ]:




