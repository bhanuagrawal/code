#include <stdio.h>
#include <iostream>
using namespace std;

void update(int &data){
	data = 5
}

int int main(int argc, char const *argv[])
{
	int a = 10;
	int b = 8;
	update(b);
	update(a);
	cout<< a;
	cout<<b;
	return 0;
}