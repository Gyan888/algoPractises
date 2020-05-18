#include <iostream>
using namespace std;

void printArray(int *arr,int size){
        int i=0;
        while(i<size){
                cout<<arr[i];
                i++;
        }
        cout <<"\n";

}


void swap(int *i,int *j){
	int temp;
	temp=*i;
	*i=*j;
	*j=temp;
}


int partition(int *arr,int low,int high){
	int pivot =arr[high];
	int i=low-1;
	for (int j=low;j<high;j++){
	  if (pivot>arr[j]){
		i++;
		swap(&arr[i],&arr[j]);
	   }
	}
	swap(&arr[i+1],&arr[high]);
	return (i+1);
}


void quickSort(int *arr,int low,int high){
	if (low<high){
		int pivot=partition(arr,low,high);
		cout <<"pivot now "<<pivot<<"low: "<<low <<",high: "<<high <<"\n";
		quickSort(arr,low,pivot-1);
		quickSort(arr,pivot+1,high);
	}	
}




int main(){
	int arr[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0}; 
	int size=sizeof(arr)/sizeof(arr[0]);
	cout <<"array before sort \n";
	printArray(arr,size);
	cout <<"array size is "<<size<<"\n";
	quickSort(arr,0,size-1);
	cout <<"Now array check \n";
	printArray(arr,size);
	return 0;
	
}

