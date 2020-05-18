#include <iostream>
#define V 9
#include <limits.h> 
#include <stdio.h> 


// here we use relaxation and greedy approach

using namespace std;


int getMinIndex(int dist[V],bool status[V]){
	int temp=INT_MAX;	
	int minIndex;
	for (int i=0;i<V;i++){
		if (!(status[i]) && dist[i]<temp){
			temp=dist[i];			
			minIndex=i;			
		}		
	}
	for (int i=0;i<V;++i){
	cout <<dist[i]<<", ";
	}
	cout<<"\n";
	cout <<"min index "<<minIndex<<"\n";
	return minIndex;
}


void printSolution(int dist[V]){
	for (int i=0; i<V; i++){
		cout <<"index "<<i<<"\t\t"<<dist[i]<<"\n";
	}
}

void djkistra(int graph[V][V],int startVertex){
	int dist[V];	
	bool status[V];
	for (int i=0;i<V;i++){
		dist[i]=INT_MAX;
		status[V]=false;
	}	
	dist[startVertex]=0;
	status[startVertex]=true;
	for (int i=0;i<V;i++){
		int minIndex=getMinIndex(dist,status);		
		status[minIndex]=true;
		int temp=INT_MAX;
		int index;
		for (int j=0;j<V;j++){ // this is the relaxation  approach ==>graph[minIndex][j]+ dist[minIndex]<dist[j]
		    if (!(status[j]) && graph[minIndex][j] && (graph[minIndex][j]+ dist[minIndex]<dist[j]) && dist[minIndex]!=INT_MAX ){
				dist[j]=dist[minIndex]+graph[minIndex][j];				
			}
		}	
	}
	printSolution(dist);
}

int main(){
	int graph[V][V]={ { 0, 4, 0, 0, 0, 0, 0, 8, 0 }, 
                        { 4, 0, 8, 0, 0, 0, 0, 11, 0 }, 
                        { 0, 8, 0, 7, 0, 4, 0, 0, 2 }, 
                        { 0, 0, 7, 0, 9, 14, 0, 0, 0 }, 
                        { 0, 0, 0, 9, 0, 10, 0, 0, 0 }, 
                        { 0, 0, 4, 14, 10, 0, 2, 0, 0 }, 
                        { 0, 0, 0, 0, 0, 2, 0, 1, 6 }, 
                        { 8, 11, 0, 0, 0, 0, 1, 0, 7 }, 
                        { 0, 0, 2, 0, 0, 0, 6, 7, 0 } }; 

	djkistra(graph,0);
	return 0;
}
