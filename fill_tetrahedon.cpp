#include<iostream>
#include<cmath>
using namespace std;
float fill_tetrahedon(int num)
{
    float h = sqrt(num*num - (num/2.0)*(num/2.0));
    float B = (1/2.0)*num*h;
    float H = sqrt((num*num) - (4/9.0)*h*h);
    return B*H/3000.0;
}
int main()
{
    cout<<"You need "<<fill_tetrahedon(100)<<" litres to fill the tetrahedon"<<"\n";
}
