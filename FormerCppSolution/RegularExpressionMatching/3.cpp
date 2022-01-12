#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool isMatch(string s, string p)
{
    if (s.size() == 0 && p.size() == 0)
        return true;
    else if (s.size() == 0)
    {
        int c = 0;
        while (p.size() >= 2 && p.at(0) != '*' && p.at(1) == '*')
        {
            if (p.size() - 2 > 0)
                p = p.substr(2, p.size() - 2);
            else
                p = "";
        }
        if (p.size() == 0)
            return true;
        else
            return false;
    }
    else if (p.size() == 0)
        return false;

    char cs = s.at(0), cp = p.at(0);
    char tmp = cp;
    if ((tmp != cs && tmp != '.') && p.size() >= 2 && p.at(1) != '*')
        return false;
    else if ((tmp != cs && tmp != '.') && p.size() >= 2 && p.at(1) == '*')
    {
        p = p.substr(2, p.size() - 2);
        return isMatch(s, p);
    }
    else if (tmp == '.' && p.size() >= 2 && p.at(1) == '*')
    {
        int i = 0;
        char cs = s.at(0), cp = p.at(0);
        char tmp = cp;
        string as = s, ap = p;
        while (as.size() >= 1)
        {
            if (ap.size() - 2 > 0 && tmp == '.' && ap.size() >= 2 && ap.at(1) == '*')
                ap = ap.substr(2, ap.size() - 2);
            else if (ap.size() - 2 == 0)
                ap = "";
            if (isMatch(as, ap))
                return true;
            if (as.size() - 1 > 0)
                as = as.substr(1, as.size() - 1);
            else
                as = "";
            i++;
        }
        while (s.size() >= 1)
        {
            if (s.size() - 1 > 0)
                s = s.substr(1, s.size() - 1);
            else
                s = "";
            if (p.size() - 2 > 0 && tmp == '.' && p.size() >= 2 && p.at(1) == '*')
                p = p.substr(2, p.size() - 2);
            else if (p.size() - 2 == 0)
                p = "";
            if (isMatch(s, p))
                return true;
            i++;
        }
        return false;
    }
    else if (tmp == cs && p.size() >= 2 && p.at(1) == '*')
    {
        int i = 0;
        char cs = s.at(0), cp = p.at(0);
        char tmp = cp;
        string as = s, ap = p;
        while (ap.size() >= 2)
        {
            if (ap.size() - 2 > 0 && ap.size() >= 2 && ap.at(1) == '*')
            {
                ap = ap.substr(2, ap.size() - 2);
                tmp = ap.at(0);
            }
            else if (ap.size() - 2 == 0)
                ap = "";
            else
                break;
            if (isMatch(as, ap))
                return true;
            // if (as.at(0) == tmp)
            //     if (as.size() - 1 > 0)
            //     {
            //         as = as.substr(1, as.size() - 1);
            //         cs = as.at(0);
            //     }
            //     else
            //         as = "";
            i++;
        }
        while (s.size() >= 1)
        {
            if (s.at(0) == cp)
                if (s.size() - 1 > 0)
                    s = s.substr(1, s.size() - 1);
                else
                    s = "";
            else
                return false;
            if (isMatch(s, p))
                return true;
            // if (p.size() - 2 > 0 && p.size() >= 2 && p.at(1) == '*')
            //     p = p.substr(2, p.size() - 2);
            // else if (p.size() - 2 == 0)
            //     p = "";
            i++;
        }
        return false;
    }
    else if ((tmp == cs || tmp == '.') && p.size() >= 2 && p.at(1) != '*')
    {
        if (s.size() - 1 > 0)
            s = s.substr(1, s.size() - 1);
        else
            s = "";
        p = p.substr(1, p.size() - 1);
        return isMatch(s, p);
    }
    else if ((tmp == cs || tmp == '.') && p.size() == 1)
    {
        if (s.size() - 1 > 0)
            s = s.substr(1, s.size() - 1);
        else
            s = "";
        p = "";
        return isMatch(s, p);
    }
    return false;
}

int main()
{
    while (1)
    {
        cout << endl
             << "Input a string please: ";
        string s;
        cin >> s;
        cout << "Input a pattern please: ";
        string p;
        cin >> p;
        bool ans = isMatch(s, p);
        if (ans)
            cout << "Matches successfully!" << endl;
        else
            cout << "Can not match!" << endl;
    }

    return 0;
}