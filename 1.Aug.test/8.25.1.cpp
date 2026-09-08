#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;
int main(){
    vector<int>scores;
    scores.push_back(80);
    scores.push_back(92);
    scores.push_back(75);
    scores.push_back(92);
    scores.push_back(88);
    scores.push_back(75);
    scores.push_back(92);
    cout<<"all scores:"<<endl;
    for(int x:scores){
        cout<<x<<" ";
    }
    cout<<'\n';
    sort(scores.begin(),scores.end());
    map<int,int>cnt;
    for(int x:scores){
        cnt[x]++;
    }
    for(auto p:cnt){
        cout<<p.first<<":"<<p.second<<endl;
    }
    return 0;
} // namespace
