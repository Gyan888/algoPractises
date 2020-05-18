import sys
class Graph:
    
    def __init__(self,vertex):        
        self.vertex=vertex
        self.graph=[[0 for i in range(vertex)] for i in range(vertex)]
        
    
    def getMin(self,toBeMin,unvisited):
        min=sys.maxsize
        minIndex=None
        for i,value in enumerate(toBeMin):
            if value<min and unvisited[i] is False:
                min=value;
                minIndex=i
        return minIndex
                    
    def printMst(self,parent,toBeMin):
        print ("parent {},weight {}".format(parent,toBeMin))
        print("min weight ",reduce(lambda x,y:x+y,toBeMin))
        
                        
    
    
    def prims(self):
        unvisited=self.vertex*[False]
        toBeMin=self.vertex*[sys.maxsize]
        toBeMin[0]=0 # setting this to minimum
        parent=self.vertex*[None]
        parent[0]=-1
        
        for i in range(self.vertex):                                    
            minindex=self.getMin(toBeMin,unvisited)
            unvisited[minindex]=True
            for i,value in enumerate(self.graph[minindex]):
                if self.graph[minindex][i]>0 and value<toBeMin[i] and unvisited[i] is False:
                    toBeMin[i]=value
                    parent[i]=minindex
        self.printMst(parent,toBeMin)
            
            
            
g=Graph(5)
g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
g.prims()
