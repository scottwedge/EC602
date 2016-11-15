// AUTHOR johnkeisling jfkeis@bu.edu
// AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu
//
// w10_wordplayer.cpp

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

void swap(char *x, char *y)
{
    char temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void permute(char *a, int l, int r)
{
    int i;
    if (l == r)
        printf("%s\n", a);
    else
    {
        for (i = l; i <= r; i++)
        {
            swap((a+l), (a+i));
            permute(a, l+1, r);
            swap((a+l), (a+i));
        }
    }
}

int main(int argc, const char * argv[]) {
    ifstream big_wordlist;
    big_wordlist.open(argv[1]);
    
    int n;
    string inword;
    cin >> inword >> n;
    
    cout << n << " " << inword << "\n";
    
    
    do
    {
        cout << inword << "\n";
    }
    while ( next_permutation(inword.begin(), inword.end()) );
    
    //permute(inchar, 0, 7);
    
    
    
    
    return 0;
}
