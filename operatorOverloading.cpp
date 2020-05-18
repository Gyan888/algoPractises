#include <iostream>
using namespace std;

class Complex{
private:
	int real;
	int imag;
public: 
	Complex(int r=0,int i=0){ // defalt destructor 
		real=r;
		imag=i;
	}
	
	Complex operator +(Complex &obj){
		Complex test;
		test.real=real+obj.real;
		test.imag=imag+obj.imag;
		return test;
		
	}
	void print(){
		cout <<"imaginary :"<<imag <<" "<<"real :"<<real <<"\n";
	}
};




int main(){
Complex Comp1(2,3);
Complex Comp2(4,5);
Complex comp3=Comp1+Comp2;
comp3.print();
return 0;


}
