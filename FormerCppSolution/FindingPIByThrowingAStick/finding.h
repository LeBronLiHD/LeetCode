#include <iostream>
#include <iomanip>
#include <random>
#include <cmath>
using namespace std;

class finding
{
private:
public:
    finding();
    ~finding();
    void findPI();
};

finding::finding()
{
}

void finding::findPI()
{
    const double pi = 3.14159265358;
    double stick_length;
    double board_width;
    cout << "Enter the width of a floorboard: ";
    cin >> board_width;
    cout << "Enter the length of the stick (must be less than " << board_width << "): ";
    cin >> stick_length;
    stick_length = (stick_length >= board_width) ? 0.9 * board_width : stick_length;
    uniform_real_distribution<double> angle{0.0, pi};
    uniform_real_distribution<double> position{0.0, board_width};
    random_device rd;
    default_random_engine engine(rd());         // random number generator
    const long signed int throws = 500'000'000; // number of random throws
    long signed int hits;                       // count of stick intersecting the board
    for (int i = 0; i < throws; i++)
    {
        double y(position(engine));
        double theta(angle(engine));
        // check if the stick crosses the edge of the board
        if (((y + 0.5 * stick_length * sin(theta)) >= board_width) ||
            ((y - 0.5 * stick_length * sin(theta)) <= 0))
            hits++;
    }
    cout << fixed << setprecision(16); // 16 decimal places
    cout << "Probability of the stick crossing the edge of a board is: "
         << static_cast<double>(hits) / throws << endl;
    cout << "PI is: " << (2 * stick_length * throws) / (board_width * hits) << endl;
    cout << "Relative error is: " << abs((2 * stick_length * throws) / (board_width * hits) - pi) / pi * 100 << "%" << endl;
    return;
}

finding::~finding()
{
}
