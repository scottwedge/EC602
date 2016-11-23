// Copyright 2016 jfkeis@bu.edu
// AUTHOR johnkeisling jfkeis@bu.edu
// AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu
//
// w10_wordplayer.cpp

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <list>
#include <numeric>
#include <map>

std::vector<int> arr;
std::vector<std::string> res;
bool e = false;

std::string printArray(int size) {
    std::string result;
    for (int i = 0; i < size; i++) {
        char letter = arr[i];
        result = result + letter;
    }
    res.push_back(result);
    std::cout << std::endl;

    return result;
}

void swap(int x, int y) {
    int temp = arr[x];
    arr[x] = arr[y];
    arr[y] = temp;

    return;
}

void permute(int k, int size) {
    int i;
    if (k == 0) {
        printArray(size);
    } else {
        for (i = k - 1; i >= 0; i--) {
            swap(i, k - 1);
            permute(k - 1, size);
            swap(i, k - 1);
        }
    }

    return;
}


int main(int argc, const char * argv[]) {
    while (e == false) {
        std::ifstream big_wordlist;
        big_wordlist.open(argv[1]);

        std::string word;
        std::vector<std::string> mymap;
        while (getline(big_wordlist, word)) {
            mymap.push_back(word);
        }

        big_wordlist.close();

        std::string inword;
        int x;

        std::cin >> inword >> x;

        if (x <= 0) {
            e = true;
            break;
        }

        int len = inword.length();

        std::cout << inword.length() << " " << inword << "\n";

        for (int i = 0; i < len; i++) {
            arr.push_back(inword[i]);
        }

        permute(len-1, x);

        std::sort(mymap.begin(), mymap.end());
        std::sort(res.begin(), res.end());
        std::vector<std::string> common;

        std::set_intersection(mymap.begin(), mymap.end(),
            res.begin(), res.end(), std::back_inserter(common));

        for (int i = 0; i < common.size(); i++) {
            std::cout << common[i] << "\n";
        }

        std::cout << "...\n";
    }
    return 0;
}
