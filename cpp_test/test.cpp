#include <iostream>
#include <math.h>
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

int main()
{
    string pizza = "pizza";
    string* food = &pizza;
    string favfood;
    int favnum;

    cout << pizza << food << *food << "\n"; 

    *food = "macs";

    cout << pizza << food << *food;

    cout << "\nwhat is your fav food: ";
    cin >> favfood;

    cout << "\nyour fav food is " << favfood;

    while (true) {
        cout << "\nthink of a number between 1 - 10";
        cin >> favnum;
        if (0 < favnum < 11) {
            break;
        } else {
            continue;
        }
        
    }
}