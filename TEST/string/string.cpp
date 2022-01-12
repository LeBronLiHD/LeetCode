#include <iostream>
#include <string>
using namespace std;

int main()
{
    string input, input2, in1, in2, in, sub, sw1, sw2, fd, fd2, er, rep;
    //.length() or .size()
    //.at(index) start from 0
    //.append(string) str1 + str2 (concatenate)
    //.insert(index, string, begin, length)
    //.assign(string) copy
    //.substr(begin, length)
    //.find(substr) (return when FIRST found)
    //.rfind(substr) (return when LAST found)
    //.erase(index)
    //.replace(index, length, string)
    cout << endl
         << "1. .length() or .size() & .append(string)" << endl;
    cout << "Input your string with getline: ";
    getline(cin, input);
    cout << "Input your string with getline: "; //cin stop when ' ' has been typed
    getline(cin, input2);
    input = input.append(input2);
    int len = input.length(); //or sum.size()
    cout << endl
         << "Your string is str1 + str2 = " << input << endl
         << "The length is: " << len << endl;

    cout << endl
         << "2. .insert(index, string, begin, length)" << endl;
    cout << "Input your str1 (least 2 elements): ";
    cin >> in1;
    cout << "Input your str2 (least 6 elements): ";
    cin >> in2;
    in = in1.insert(2, in2, 2, 4);
    cout << "After in1.insert(2, str2, 2, 4) : " << in << endl;

    cout << endl
         << "3. substr(begin, length)" << endl
         << "sub = \"abcdefghijklmnopqrstuvwxyz\"" << endl;
    sub = "abcdefghijklmnopqrstuvwxyz";
    cout << "least 10 elements, can not use cin or getline" << endl
         << "sub.substr(4, 6) is：" << sub.substr(4, 6) << endl;

    cout << endl
         << "4. swap(string)" << endl;
    cout << "Input your str1: ";
    cin >> sw1;
    cout << "Input your str2: ";
    cin >> sw2;
    cout << endl
         << "str1: " << sw1 << endl
         << "str2: " << sw2 << endl
         << endl;
    sw1.swap(sw2);
    cout << "str1: " << sw1 << endl
         << "str2: " << sw2 << endl;

    cout << endl
         << "5. .find(substr)" << endl;
    cout << "Input your string: ";
    cin >> fd;
    cout << "Input the substr: ";
    cin >> fd2;
    cout << "for find:" << endl;
    if (fd.find(fd2) >= 0 && fd.find(fd2) < fd.size())
        cout << "The location is: " << fd.find(fd2) << endl;
    else
        cout << "Can not find!" << endl;
    cout << "for reverse find" << endl;
    if (fd.rfind(fd2) >= 0 && fd.rfind(fd2) < fd.size())
        cout << "The location is: " << fd.rfind(fd2) << endl;
    else
        cout << "Can not find!" << endl;

    cout << endl
         << "6. erase(index)" << endl;
    cout << "Input your string(at least 5 elements): ";
    cin >> er;
    cout << "er.erase(5) = " << er.erase(5) << endl;

    cout << endl
         << "7. .replace(index, length, string)" << endl;
    cout << "Input your string(at least 10 elements): ";
    cin >> rep;
    cout << "string.replace(5,5,\"##########\") = " << rep.replace(5, 5, "##########") << endl;
    return 0;
}