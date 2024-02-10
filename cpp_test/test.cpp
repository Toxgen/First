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
    if (x == 0 && y == 0) {
        throw runtime_error("blud is dividing by 0\n'");
    }
    return x / y;
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

            cout << "your number is: " << stupid;

        } else {
            return -1;
        }

    }
            
        return 1;
}