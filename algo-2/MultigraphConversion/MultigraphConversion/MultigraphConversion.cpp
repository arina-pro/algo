// MultigraphConversion.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <list>

int main() {
    std::list<int> arr[4]{ {}, { 1, 2, 2 }, { 0, 2, 3, 3 }, { 3, 1 } };
    const int arrSize = (sizeof(arr) / sizeof(*arr));
    int checkingList[arrSize];
    for (int i = 0; i < arrSize; i++) {
        std::cout << "Adjacency list for vertex " << i << ":";
        if (arr[i].size() != 0) {
            for (std::list<int>::iterator iter = arr[i].begin(); iter != arr[i].end(); iter++) {
                std::cout << " " << *iter;
            }
        }
        std::cout << "\n";
    }
    for (int i = 0; i < arrSize; i++) {
        std::cout << "Adjacency list for vertex " << i << ":";
        if (arr[i].size() != 0) {
            for (std::list<int>::iterator iter = arr[i].begin(); iter != arr[i].end(); iter++) {
                std::cout << " " << *iter;
            }
        }
        std::cout << "\n";
    }
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
