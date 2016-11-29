// AUTHOR johnkeisling jfkeis@bu.edu
// AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu
//
// w10_wordplayer.cpp

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <typeinfo>
#include <algorithm>
#include <cassert>
#include <iterator>
#include <list>
#include <numeric>
#include <map>

using namespace std;

std::vector<int> arr;
std::vector<string> res;

string printArray(int size){
    string result;
    for (int i=0;i<size;i++)
    {
        char letter = arr[i];
        result = result + letter;
        //std::cout << letter << " ";
    }
    res.push_back(result);
    std::cout << std::endl;
    
    return result;
}

void swap(int x, int y){
    int temp = arr[x];
    arr[x]=arr[y];
    arr[y]=temp;
    
    return;
}

void permute(int k,int size){
    int i;
    if (k==0)
        printArray(size);
    else{
        for (i=k-1;i>=0;i--){
            swap(i,k-1);
            permute(k-1,size);
            swap(i,k-1);
        }
    }
    
    return;
}


int main(int argc, const char * argv[]) {
    
    ifstream big_wordlist;
    big_wordlist.open(argv[1]);
    
    string word;
    vector<string> mymap;
    while (getline(big_wordlist, word))
    {
        mymap.push_back(word);
    }
    
    big_wordlist.close();
    
    string inword;
    int x;
    
    cin >> inword >> x;
    int len = int(inword.length());
    
    cout << inword.length() << " " << inword << "\n";
    
    for(int i=0;i<len;i++)
    {
        arr.push_back(inword[i]);
    }

    permute(len-1,x);
    
    for(int i=0;i<res.size();i++)
    {
        cout << res[i] << "\n";
    }
    
    sort(mymap.begin(), mymap.end());
    sort(res.begin(), res.end());
    vector<string> common;
    
    set_intersection(mymap.begin(), mymap.end(), res.begin(), res.end(), back_inserter(common));
    
    for(int i=0;i<common.size();i++)
    {
        cout << common[i] << "\n";
    }
    
    
    return 0;
}
