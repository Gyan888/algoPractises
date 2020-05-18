#include <iostream>
#include <vector>
using namespace std ;
class Graph {
 public :
	Graph(int size);
	~Graph();
	void printRelation();
	void pushGraph(int node,int relatedNode);
 private:
	vector <int > *Vertices=NULL;
	int size ;
};

Graph::Graph(int size){
 	cout <<"Constructor is called "<<"\n";
 	this->size=size;
	Vertices=new vector<int >[size];
}

Graph::~Graph(){
	cout <<"Destructor is called ";
	delete [] Vertices;

}

void Graph::pushGraph(int node,int relatedNode){
	Vertices[node].push_back(relatedNode);
	Vertices[relatedNode].push_back(node);		
}

void Graph::printRelation(){
	for(int i=0;i<this->size;i++){
	    cout << "\n Adjacency list of vertex "
             << i << "\n head "; 
	    vector<int>::iterator it;
	    for (it=Vertices[i].begin();it!=Vertices[i].end();it++){
	        cout << "-> " << *it; 		
	    }
	cout <<"\n";	  
	}
}

int main(){
    Graph *myGraph=new Graph(5);// this is an undirected graph
    myGraph->pushGraph(0, 1); 
    myGraph->pushGraph(0, 4); 
    myGraph->pushGraph(1, 2); 
    myGraph->pushGraph(1, 3); 
    myGraph->pushGraph(1, 4); 
    myGraph->pushGraph(2, 3); 
    myGraph->pushGraph(3, 4);
    myGraph->printRelation();
    delete myGraph;
    return 0; 
}









