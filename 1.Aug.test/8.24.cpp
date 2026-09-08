#include <iostream>
#include <string>
#include <map>
using namespace std;
int main(){
    string s;
    cout <<"enter a string:"<<endl;
    getline(cin,s);
    map<char,int> cnt;
    for(char c : s){
        cnt[c]++;
    }
    for(auto p : cnt){
        cout<<p.first<<":"<<p.second<<endl;
    }
    return 0;
}
