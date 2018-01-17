#include <iostream>

using namespace std;

int suma(int n1, int n2){
	return n1 + n2;
}

int resta(int n1, int n2){
	return n1 - n2;
}

int main(){
	int n1, n2;

	n1 = 3;
	n2 = 2;

	cout<<suma(n1,n2)<<endl;

}