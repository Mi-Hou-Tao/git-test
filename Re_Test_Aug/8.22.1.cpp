#include<iostream>
#include<string>
#include<climits>
using namespace std;
int main(){
    string s;
    cout << "Enter a string:";
    cin >> s;
    int count[26] = {0};
    for (int i = 0; i < s.length(); i++){
    int index = s[i] - 'a';
    count[index]++;
    }
    for (int i = 0; i < 26; i++){
        if(count[i]!=0){
            char c = 'a' + i;
            cout<<c<<":"<<count[i]<<endl;
           }

    }
    int maxCount = 0;
    char maxindex = 'a';
    for (int i = 0;i < 26; i++){
        if(count[i] > maxCount){
            maxCount = count[i];
            maxindex = 'a' + i;
        }
    }
    cout << "The character with the maximum frequency is: " << maxindex << " with a count of " << maxCount << endl;
    int minCount = INT_MAX;
    char minindex = 'a';
    for (int i = 0; i < 26; i++){
        if(count[i] != 0 && count[i] < minCount){
            minCount = count[i];
            minindex = 'a' + i;
        }
    }   
    cout << "The character with the minimum frequency is: " << minindex << " with a count of " << minCount << endl;
    
    return 0;
}
    
