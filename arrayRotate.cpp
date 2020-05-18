#include<iostream>
#include<vector>
using namespace std;

void printArray(int *arr,int size){
        int i=0;
        while(i<size){
                cout<<arr[i];
                i++;
        }
        cout <<"\n";

}




void arrayRotate(int *arr,int size,int RotateBy){
	vector <int> g1;
	if (RotateBy>=size){
                 return ;
        }
	for (int i=0;i<size;i++){
		
		g1.push_back(arr[i]);
		
	}
	
		
 
}


int main(){
 int arr[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
 int size=sizeof(arr)/sizeof(arr[0]);
 arrayRotate(arr,size,3);
 return 0;

}
