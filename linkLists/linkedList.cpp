#include<iostream>
using namespace std;


class Node{
   public:
	int data;
	Node *next;
};

void printNodes(Node * node){
	if (node->next==NULL){
		cout <<"node data :"<<node->data<<"\n";
		return; 
	}
	cout <<"node data :"<<node->data<<"\n";
	node=node->next;
	printNodes(node);
}


// this function is pushing a new element at the front of a linked list

// double star act like a pointer of a ponter
void push(Node **headref , int  pointerData){
	Node *newNode=new Node();
	newNode->data=pointerData;
	newNode->next=*(headref);
	*(headref)=newNode; //new Node will become the head node 
}


// pushing the element at the end of the link list 
void pushLast(Node **headref ,int NewData){
	Node * newNode=new Node();
	Node *fstNode=NULL;
	newNode->next=NULL;
	newNode->data=NewData;
	fstNode=*headref; // now first node pointer is assigned to new node 
	while(fstNode->next!=NULL){
	   fstNode=fstNode->next;	
	}		
	fstNode->next=newNode;	
}


void deleteElement(Node **headref,int key){
	Node *prev=new Node();
	Node *temp =new Node();
	temp=*(headref);
	if (temp->data==key){
                  delete temp;
                  *headref=temp->next;
                  return ;          
	}
	while(temp->next!=NULL){
		prev=temp;
		temp=temp->next	;
		if(temp->data==key){
		  prev->next=temp->next;
		  delete temp;
		  break;
		}				
	}
}


int main(){
	Node *first =new Node(); // setting null pointer before assignment 
	Node *second=new Node();
	Node *third=new Node();
	Node *fourth=new Node();
	first->data=10;
	first->next=second;
	second->data=13;
	second->next=third;
	third->data=44;
	third->next=fourth;
	fourth->data=54;
	fourth->next=NULL;
	cout <<"first node addredd "<<first<<"\n";
	cout <<"before insertion :\n";
	printNodes(first);
	deleteElement(&first,44);
	cout <<"after insertion \n";
	printNodes(first);
	return 0;
}

