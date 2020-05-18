#include <iostream>
using namespace std;

class Node{
	public :int data;
	Node *next;
};

void getNext(Node *n){
     cout <<"node data "<<n->data <<"\n";
	if (n->next==NULL){
	 return;
	}
     getNext(n->next);
	
}


// this will add the new node at the front of linked list
// here we are using pointer of pointer as it allows to change the head directly instead of  retuning the pointer 
// if we use the single pointer then we have to return the pointer in return 
void insertion(Node** headref,int data){	
	Node * newNode=new Node();
	newNode->next=*(headref); // new Node next will become the head pointer ;
	newNode->data=data;
	*headref=newNode;// Now the new element will become the first element in a linked list
}


// insertion head using a single pointer 
Node * insertHead(Node *head,int data){
	Node * newNode=new Node();
	newNode->data=data;
	newNode->next=head;
	return newNode;
}

void deleteNode(Node** headref,int data ){
	Node * temp=new Node();
	Node * prev=new Node();
	temp=*(headref);
	if (temp->data==data){
                   *(headref)=temp->next;
                   delete temp;
                   return ;
        }
	while(temp->next!=NULL){
		prev=temp;	
		temp=temp->next;
		if(temp->data==data){
		   prev->next=temp->next;
		   delete temp;
		   break;		   
		}
	}		
}

int main()
{
Node *head =new Node();
Node *first=new Node();
Node *last=new Node();
head->data=10;
head->next=first;
first->data=40;
first->next=last;
last->data=70;
last->next=NULL;
cout <<"Before insertion \n";
getNext(head);
head=insertHead(head,66);
cout <<"After insertion \n";
getNext(head);
deleteNode(&head,66);
cout <<"after deletion\n";
getNext(head);
return 0;
}


