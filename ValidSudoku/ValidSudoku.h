#include <iostream>
#include <iomanip>
#include <vector>
#include <unordered_map>
#include <stack>
#include <string>
#include <random>

using namespace std;

class ValidSudoku
{
private:
    vector<vector<char>> board;
    unordered_map<char, int> count;
    vector<char> nineChars;

public:
    ValidSudoku(vector<vector<char>> B);
    ~ValidSudoku();
    bool isValidSudoku();
    bool check(vector<char> &nineChars);
    void display(bool ans);
    void refersh();
};

ValidSudoku::ValidSudoku(vector<vector<char>> B) : board(B)
{
    refersh();
}

bool ValidSudoku::isValidSudoku()
{
    // first we check each row of the table
    // int rowsNumber = board.size();
    for (int i = 0; i < 9; i++)
    {
        refersh();
        nineChars = board.at(i);
        if (check(nineChars))
            continue;
        else
            return false;
    }
    // then we check each column of the board
    for (int j = 0; j < 9; j++)
    {
        refersh();
        for (int i = 0; i < 9; i++)
            nineChars.push_back(board.at(i).at(j));
        if (check(nineChars))
            continue;
        else
            return false;
    }
    // finally we check each cube of the board
    for (int i = 0; i < 9; i++)
    {
        refersh();
        for (int j = 0; j < 9; j++)
            nineChars.push_back(board.at((i / 3) * 3 + j / 3).at((i % 3) * 3 + j % 3));
        if (check(nineChars))
            continue;
        else
            return false;
    }
    return true;
}

bool ValidSudoku::check(vector<char> &nineChars)
{
    // int size = nineChars.size();
    for (int i = 0; i < 9; i++)
    {
        count[nineChars.at(i)]++;
        if (nineChars.at(i) != '.' && count[nineChars.at(i)] > 1) // at lease two same numbers
            return false;
    }
    return true;
}

void ValidSudoku::display(bool ans)
{
    cout << "calculation done at " << this << endl;
    switch (ans)
    {
    case true:
        cout << "this is a valid sudoku" << endl;
        break;
    case false:
        cout << "this is NOT a valid sudoku" << endl;
        break;
    }
}

void ValidSudoku::refersh()
{
    nineChars.clear();
    for (char i = '1'; i <= '9'; i++)
        count[i] = 0;
    count['.'] = 0;
}

ValidSudoku::~ValidSudoku()
{
}
