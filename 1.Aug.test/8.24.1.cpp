#include<iostream>
#include<string>
using namespace std;
class Dog{
public:
    string name;
    int age;

void run(){
    cout<<age<<"-year-old dog "<<name<<" is barking"<<endl;
}

};
int main(){
    Dog a;
    a.name="xiaohuang";
    a.age=1;
    a.run();
    return 0;


}