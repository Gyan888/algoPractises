class Graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.graph={}
        
    def addEdge(self,u,v,w):
        self.graph[(u,v)]=w
                    

    def getParent(self,parent,i):
        if parent[i] is -1:
            return i
        else:
            return self.getParent(parent,parent[i])
    
    def checkCycle(self,parent,val):                                                
        x=self.getParent(parent,val[1])
        y=self.getParent(parent,val[0])
        if (x is y):            
            return True
        parent[y]=x
        return False
        
    def kruskal(self):
        parent=self.vertex*[-1] # this array is used to find if the given array forming a circle 
        sortedArray=sorted(self.graph.items(),key=lambda x:x[1])        
        mst=[]
        for i,value in enumerate(sortedArray):
            if (not self.checkCycle(parent,value[0])):
                mst.append((value))
        print("Final mst from kruskal ",mst)
            

            
            
        
    

g=Graph(4)
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
g.kruskal()       
        
        


