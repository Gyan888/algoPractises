from collections import defaultdict
class Graph:
    def __init__(self,vertex):
        self.vertex=vertex        
        self.graph=defaultdict(list)
    
    def addEdge(self,vertex,u):
        self.graph[vertex].append(u)
            
    
    def pushToStack(self,u,stack,isVisited):
        isVisited[u]=True                        
        for i in self.graph[u]:
            if not isVisited[i]:
                self.pushToStack(i,stack,isVisited)
        stack.insert(0,u)
        
            
                    
    def topologicalSort(self):
        isVisited=self.vertex*[False]     
        stack=[]   
        for i in range(self.vertex):
            if not isVisited[i]:
                self.pushToStack(i,stack,isVisited)
        print(stack)                
                        

g=Graph(6)
g.addEdge(5, 2) 
g.addEdge(5, 0) 
g.addEdge(4, 0) 
g.addEdge(4, 1) 
g.addEdge(2, 3) 
g.addEdge(3, 1) 
g.topologicalSort()