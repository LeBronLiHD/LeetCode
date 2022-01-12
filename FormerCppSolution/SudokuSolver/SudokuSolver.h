#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <stack>
#include <unordered_map>
#include <random>
#include <algorithm>

#define SIZE 9

using namespace std;

class SudokuSolver
{
private:
    vector<vector<char>> board;
    vector<vector<int>> countValid;
    // count the number of valid choices in each blank unit
    // and if the countValid == 1, means the unit have only one choice
    vector<char> NINE = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
    vector<char> tempValidCube;
    vector<char> tempValidRow;
    vector<char> tempValidColumn;
    // vector<char> temp;
    unordered_map<char, int> document;
    int emptyUnits;

public:
    SudokuSolver(vector<vector<char>> B);
    ~SudokuSolver();
    void solveSudoku();
    void searchCube(int x, int y);
    void searchRow(int x, int y);
    void searchColumn(int x, int y);
    int countProcess();
    void display();
    void refreshAll();
    void refreshDoc();
};

SudokuSolver::SudokuSolver(vector<vector<char>> B) : board(B)
{
    cout << "constructor called" << endl;
    vector<int> element;
    for (size_t i = 0; i < SIZE; i++)
    {
        // initialization: assign zero for all 9 * 9 units
        for (size_t j = 0; j < SIZE; j++)
            element.push_back(0);
        countValid.push_back(element);
    }
    for (char i = '1'; i <= '9'; i++)
    {
        pair<char, int> tempElement(i, 0);
        document.insert(tempElement);
    }
    // calculate number of empty units
    emptyUnits = 0;
    for (size_t i = 0; i < SIZE; i++)
    {
        for (size_t j = 0; j < SIZE; j++)
            if (board.at(i).at(j) == '.')
                emptyUnits++;
    }
}

SudokuSolver::~SudokuSolver()
{
    cout << "destructor called" << endl;
}

void SudokuSolver::solveSudoku()
{
    // general idea:
    // for (size_t i = 0; i < SIZE; i++)
    // {
    //     for (size_t j = 0; j < SIZE; j++)
    //     {
    //         if(countValid.at(i).at(j) == 1)
    //             board.at(i).at(j) = targetValue;
    //         solveSudoku();
    //     }
    // }
    if (!emptyUnits)
        return;
    for (size_t xOverall = 0; xOverall < SIZE; xOverall++)
    {
        for (size_t yOverall = 0; yOverall < SIZE; yOverall++)
        {
            refreshAll();
            if (board.at(xOverall).at(yOverall) != '.')
                continue;
            // if not '.', meaning this unit exists number, continue
            else
            {
                searchCube(xOverall, yOverall); // sorted
                searchRow(xOverall, yOverall);
                searchColumn(xOverall, yOverall);
                countValid.at(xOverall).at(yOverall) = countProcess();
                if (countValid.at(xOverall).at(yOverall) == 1) // only one valid choice
                {
                    board.at(xOverall).at(yOverall) = tempValidCube.at(0); // fill it in
                    emptyUnits--;
                }
            }
        }
    }
    solveSudoku(); // iteration
}

void SudokuSolver::searchCube(int x, int y)
{
    x /= 3, y /= 3;
    for (size_t i = 0; i < SIZE; i++) // construct the vector of cube elements
        if (board.at(x + i / 3).at(y + i % 3) != '.')
            document.at(board.at(x + i / 3).at(y + i % 3))++;
    // for (unordered_map<char, int>::iterator it = document.begin(); it != document.end(); it++)
    for (char i = '1'; i <= '9'; i++)
    {
        if (document.at(i) == 0)
            tempValidCube.push_back(i);
    }
}

void SudokuSolver::searchRow(int x, int y)
{
    for (size_t i = 0; i < SIZE; i++)
        if (board.at(x).at(i) != '.')
            document.at(board.at(x).at(i))++;
    for (char i = '1'; i <= '9'; i++)
    {
        if (document.at(i) == 0)
            tempValidRow.push_back(i);
    }
}

void SudokuSolver::searchColumn(int x, int y)
{
    for (size_t i = 0; i < SIZE; i++)
        if (board.at(i).at(y) != '.')
            document.at(board.at(i).at(y))++;
    for (char i = '1'; i <= '9'; i++)
    {
        if (document.at(i) == 0)
            tempValidColumn.push_back(i);
    }
}

int SudokuSolver::countProcess()
{
    tempValidCube.insert(tempValidCube.end(), tempValidRow.begin(), tempValidRow.end());
    tempValidCube.insert(tempValidCube.end(), tempValidRow.begin(), tempValidRow.end());
    sort(tempValidCube.begin(), tempValidCube.end());                                   // sort it
    for (vector<char>::iterator it = tempValidCube.begin(); it != tempValidCube.end();) // De-duplication
    {
        if ((*it++) == (*it))
            tempValidCube.erase(it);
    }
    return SIZE - tempValidCube.size();
}

void SudokuSolver::display()
{
    cout << endl
         << "calculation done!" << endl
         << endl;
    for (size_t i = 0; i < SIZE; i++)
    {
        cout << "[  ";
        for (size_t j = 0; j < SIZE; j++)
            cout << board.at(i).at(j) << "  ";
        cout << "]" << endl;
    }
}

void SudokuSolver::refreshAll()
{
    tempValidCube.clear();
    tempValidRow.clear();
    tempValidColumn.clear();
    // temp.clear();
    for (size_t i = 0; i < SIZE; i++)
        for (size_t j = 0; j < SIZE; j++)
            countValid.at(i).at(j) = 0;
    // for (char i = '1'; i <= '9'; i++)
    //     document.at(i) = 0;
    // no need
}

void SudokuSolver::refreshDoc()
{
    for (char i = '1'; i <= '9'; i++)
        document.at(i) = 0;
}