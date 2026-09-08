#include <iostream>
#include <string>
using namespace std;
int main() {
    string s;
    cout << "Enter a string: ";
    cin >> s;
        int count[26] = {0};
        for (char c : s) {
            count[c - 'a']++;
        }
        int result = -1;
        for (int i = 0; i < s.length(); i++) {
            if (count[s[i] - 'a'] == 1) {
                result = i;
                break;
            }
        }
       if (result != -1) {
            cout << "The index of the first non-repeating character is: " << result << endl;
        } else {
            cout << "No non-repeating character found." << endl;
        }
        return 0;
    }



