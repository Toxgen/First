#include <iostream>
#include <math.h>
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

int main()
{
    float x, y;
    string foo;

    cout << "type in first num \n";
    cin >> x;

    cout << "type in second num \n";
    cin >> y;

    cout << "add, subtract, multiply, or divide? \n";
    while (true) {

        cin >> foo;
        if (foo == "multiply") {
            
        }
    }

}

float multiply(float x, float y)
{
    return x * y;
}

float addition(float x, float y)
{
    return x + y;
}

float subtraction(float x, float y)
{
    return x - y;
}

float division(float x, float y)
{
    if (x && y == 0) {
        return -1;
    } else {
        return x / y;
    }
}