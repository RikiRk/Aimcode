#include<iostream>
using namespace std;   
    int main () 
{
    int i,n,fact=1;
    cout<<"Enter the posetive integer"<<endl;
    cin>>n;
    for(i=1;i<=n;i++)
    {
    fact *= i;
	}
	cout<<"Your factorial number is"<<n<<endl;
	return 0;
	
}
