#include <iostream>
#include <typeinfo>
#include <limits>

using namespace std;

float add(int x, int y) 
{
    return x + y;
}

float subtract(int x, int y) 
{
    return x - y;
}

float multiply(int x, int y) 
{
    return x * y;
}

float division(int x, int y) 
{
    float z;
    return z = (x != 0 && y != 0) ? x / y : -1.01;
}

int main()
{
    float num1, num2, stupid;
    string user;
    while (true) {
        cout << "enter a number: ";
        
        if (!(cin >> num1)) {        
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "\n";
            continue;
        } else {
            cout << "\n";
        }

        cout << "enter some other number: ";

        if (!(cin >> num2)) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "\n";
            continue;
        } else {
            cout << "\n";
        }

        cout << '\n' << "+, -, /, or *? ";
        cin >> user;
        cout << '\n';

        if (user == "+") {
            cout << "your number is: " << add(num1, num2);

        } else if (user == "-") {
            cout << "your number is: " << subtract(num1, num2);

        } else if (user == "*") {
            cout << "your number is: " << multiply(num1, num2);
            
        } else if (user == "/") {
            stupid = division(num1, num2);

            cout << '\n' << stupid << '\n';

            if (abs(stupid - (-1.01)) > 0.0001) {
                cout << "your number is: " << stupid;

            } else {
                cout << "your number is: 0";
            }

        } else {
            return -1;
        }

    }
            
        return 1;
}