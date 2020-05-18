#include <iostream>
#include <vector>
using namespace std;

int main(){
    if (__cplusplus == 201703L) std::cout << "C++17\n";
    else if (__cplusplus == 201402L) std::cout << "C++14\n";
    else if (__cplusplus == 201103L) std::cout << "C++11\n";
    else if (__cplusplus == 199711L) std::cout << "C++98\n";
    else std::cout << "pre-standard C++\n";
    vector<int > g1;
    for (int i=0;i<10;i++){
  	g1.push_back(i);
	}
    cout << "Size : " << g1.size(); 
    cout << "\nCapacity : " << g1.capacity(); 
    cout << "\nMax_Size : " << g1.max_size();  
    cout << "\nVector elements are: "; 
    vector<int>::iterator it; 
    for (it = g1.begin(); it != g1.end(); it++) 
        cout << *it << " ";
    return 0; 
}
