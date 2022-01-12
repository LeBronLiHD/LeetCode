#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <random>
using namespace std;

#define LowerCaseEnglishLetters 123
// ASCII table: 'z' = 122
// we only need 26 elements: 97-122

class Substring
{
private:
    string S;
    vector<string> L;

public:
    Substring(string str, vector<string> wor);
    ~Substring();
    vector<int> findSubstring();
    double hash(double f, double code[], string &word);
    void display(vector<int> &ans);
    void printCode(double code[]);
    void printValues(vector<double> &values);
};

Substring::Substring(string str, vector<string> wor) : S(str), L(wor)
{
}
// The general idea:
// Construct a hash function f for L, f: vector<string> -> int,
// Then use the return value of f to check whether a substring is a concatenation of all words in L.
//
// f has two levels, the first level is a hash function f1 for every single word in L.
// f1 : string -> double
// So with f1, L is converted into a vector of float numbers
//
// Then another hash function f2 is defined to convert a vector of doubles into a single int.
// Finally f(L) := f2(f1(L))
//
// To obtain lower complexity, we require f1 and f2 can be computed through moving window.
// The following corner case also needs to be considered:
// f2(f1(["ab", "cd"])) != f2(f1(["ac", "bd"]))
// There are many possible options for f2 and f1.
// The following code only shows one possibility (probably not the best),
// f2 is the function "hash" in the class,
// f1([a1, a2, ... , an]) := int( decimal_part(log(a1) + log(a2) + ... + log(an)) * 1'000'000'000 )

vector<int> Substring::findSubstring()
{
    cout << fixed << setprecision(16);
    // 16 decimal places
    uniform_real_distribution<double> uniform(0.0, 1.0);
    default_random_engine seed;
    double code[LowerCaseEnglishLetters];
    for (auto &d : code)
        d = uniform(seed);
    // for(size_t i = 0; i < 128; i++)
    //      code[i] = uniform(seed);
    printCode(code);
    double f = uniform(seed) / 5.0 + 0.8;
    // f \in {0.8, 1.0}
    cout << "f\t= " << f << endl;
    double value = 0;

    // The complexity of the following for loop is O(L.size( ) * nW).
    for (auto &word : L)
        value += log(hash(f, code, word));
    cout << "value\t= " << value << endl
         << "floor\t= " << floor(value) << endl;

    long signed int unit = 1'000'000'000;
    long signed int key = (value - floor(value)) * unit;
    cout << "key\t= " << key << endl;
    int nS = S.size(), nL = L.size(), nW = L[0].size();
    double fn = pow(f, nW - 1.0);
    cout << "fn\t= " << fn << endl;

    vector<int> result;
    // the answer
    if (nS < nW)
        return result;
    // initialization
    vector<double> values(nS - nW + 1);
    string word(S.begin(), S.begin() + nW);
    values.at(0) = hash(f, code, word); // value of the first word

    // Use a moving window to hash every word with length nW in S to a float number,
    // which is stored in vector values[]
    // The complexity of this step is O(nS).
    for (int i = 1; i <= nS - nW; ++i)
        values[i] = (values[i - 1] - code[S[i - 1]] * fn) * f + code[S[i + nW - 1]];
    // corresponded to hash()
    // minus with code[S[i - 1]] * fn means et rid of the head chat of value[i - 1]
    // and maintain the rest elements of value[i - 1]
    // then multiply with f and plus code[tail char of current word] equals to hash()
    printValues(values);
    // or the code below:
    // for (int i = 1; i <= nS - nW; i++)
    // {
    //     word.assign(S, i, nW);
    //     values.at(i) = hash(f, code, word);
    // }
    // printValues(values);

    // This for loop will run nW times, each iteration has a complexity O(nS/nW)
    // So the overall complexity is O(nW * (nS / nW)) = O(nS)
    for (int i = 0; i < nW; ++i)
    {
        int j0 = i, j1 = i, k = 0;
        double sum = 0.;

        // Use a moving window to hash every L.size() continuous words with length nW in S.
        // This while loop will terminate within nS/nW iterations since the increasement of j1 is nW,
        // So the complexity of this while loop is O(nS / nW).
        while (j1 <= nS - nW)
        {
            sum += log(values.at(j1));
            ++k; // words counter
            j1 += nW;
            if (k == nL)
            {
                int key1 = (sum - floor(sum)) * unit;
                if (key1 == key)
                    result.push_back(j0);
                sum -= log(values.at(j0));
                --k;
                j0 += nW;
            }
        }
    }
    return result;
}

// The complexity of this function is O(nW).
double Substring::hash(double f, double code[], string &word)
{
    double result = 0.0;
    for (auto &c : word)
        result = result * f + code[c];
    return result;
    // or the code below:
    // int size = word.length() - 1;
    // double result = 0.0;
    // for(int i = size; i >= 0 ; i--)
    // {
    //      result += code[word.at(i)] * pow(f, size - i);
    // }
    // return result;
}

void Substring::display(vector<int> &ans)
{
    cout << "calculation done!" << endl;
    cout << "the result is below:" << endl;
    if (ans.empty())
    {
        cout << "NULL" << endl;
        return;
    }
    int size = ans.size();
    cout << ans.at(0) << " ";
    for (int i = 1; i < size; i++)
    {
        cout << "-> " << ans.at(i) << " ";
    }
    cout << endl;
    return;
}

void Substring::printCode(double code[])
{
    cout << endl
         << "The code table is:" << endl;
    for (size_t i = 97; i < LowerCaseEnglishLetters; i++)
    {
        if (i % 8 == 0)
            cout << endl;
        cout << code[i] << " ";
    }
    cout << endl;
}

void Substring::printValues(vector<double> &values)
{
    cout << endl
         << "The values table is:" << endl;
    int size = values.size();
    for (size_t i = 0; i < size; i++)
    {
        if (i % 8 == 0)
            cout << endl;
        cout << values.at(i) << " ";
    }
    cout << endl;
}

Substring::~Substring()
{
}
