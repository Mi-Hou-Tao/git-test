#include <iostream>
using namespace std;

int main() {
    int original,n, m = 0;
    cout << "Enter a number: ";
    cin >> n;
    original = n;
    while (n >= 1) {
    int last_digit = n % 10;
    m = m * 10 + last_digit;
    n /= 10;
    }
    if (m == original) {
        cout << "The number is a palindrome." << endl;
    } else {
        cout << "The number is not a palindrome." << endl;
    }
    return 0;
}