from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=defaultdict(list)
    
    def getParent(self,parent,i):
        if parent[i]==-1:
            return i
        else:
            return self.getParent(parent,parent[i])
            
    def addEdge(self,vertice,edge):
        """
        this is going to add the edges in vertices 
        """
        self.graph[vertice].append(edge)
                
    
    
    def checkCycle(self):
        parent=self.vertices*[-1]
        for vertice in self.graph:
            for i in self.graph[vertice]:
                x=self.getParent(parent,vertice)
                y=self.getParent(parent,i)                
                if x==y:
                    print (parent)
                    return True
                parent[y]=x  
                 
        
    
g=Graph(7)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(6,0)
print(g.checkCycle())        
        
        
        
    
        
    