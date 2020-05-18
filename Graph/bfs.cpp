#include <iostream>
#include <vector>
#include <list> 
using namespace std;

class Graph {
 public :
        Graph(int size);
        ~Graph();
        void printRelation();
        void pushGraph(int node,int relatedNode);
		void bfs(int node );
		void dfs();
		void chkDfs(bool * arr,int node);
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
}

void Graph::bfs(int node){
	list <int >l1;
	l1.push_back(node);
	bool chckStatus[size];
	for(int i=0;i<this->size;i++){
	   chckStatus[i]=false;	
	}
	chckStatus[node]=true;	
	vector <int >::iterator it;
	while(!l1.empty()){			
	     int s=l1.front();
	     l1.pop_front();
	     cout <<s<<"\n";
	     for (it=Vertices[s].begin();it!=Vertices[s].end();it++){
		    if (!chckStatus[*it]){
			l1.push_back(*it);
			chckStatus[*it]=true;
	    	}
	    }
	}
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
	Graph *g=new Graph(5);	
	vector <int >adjNodes;
	g->pushGraph(0, 1) ;
	g->pushGraph(0, 2) ;
	g->pushGraph(1, 2) ;
	g->pushGraph(2, 0) ;
	g->pushGraph(2, 3) ;
	g->pushGraph(3, 3) ;
	//g->bfs(2);
	g->dfs();
	cout <<"\n";
	delete g;
 	return 0;
}
