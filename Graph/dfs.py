from collections import defaultdict

class Graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.graph=defaultdict(list)
        
    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)
    
    def transversal(self,isVisited,i):
        print("Node is ->",i)
        isVisited[i]=True
        for node in self.graph[i]:
            if not isVisited[node]:
                self.transversal(isVisited,node)
                    
        
    def dfs(self,node):
        isVisited=[]
        for i in range(self.vertex):
            isVisited.append(False)
        
        self.transversal(isVisited,node)
            
            
g=Graph(4)
g.addEdge(0, 1); 
g.addEdge(0, 2); 
g.addEdge(1, 2); 
g.addEdge(2, 0); 
g.addEdge(2, 3); 
g.addEdge(3, 3); 
g.dfs(2)

        
            