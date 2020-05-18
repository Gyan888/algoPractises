class Puzzle:
    def __init__(self,rows,columns):
        self.rows=rows
        self.columns=columns        
        self.graph=[]
    

    def findWords(self,dict,isVisited,str,i,j):
        isVisited[i][j]=True
        str+=self.graph[i][j]
        print(str)  
        if str in dict:
            print("string contains is ",str)
        for row in range(i-1,i+2):
            for col in range(j-1,j+2):                                                 
                if (row<self.rows and col<self.columns and row>=0 and col>=0 and not isVisited[col][row]):                      
                    self.findWords(dict,isVisited,str,row,col)
        
        print("str ",str)
        isVisited[i][j]=False

        

    def match(self,dict):
        isVisited=[[False for i in range(self.rows)] for i in range(self.columns)]
        str=""
        # for i in range(self.rows):
        #     for j in range(self.columns):
        print isVisited
        self.findWords(dict,isVisited,str,0,0)        
        
        
        

x=Puzzle(3,3)
x.graph=[['G', 'I', 'Z'], 
         ['U', 'E', 'K'], 
         ['Q', 'S', 'E']]
x.match(["GEEKS"])        
        
        
        
    