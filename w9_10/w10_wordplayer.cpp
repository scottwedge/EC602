 // AUTHOR johnkeisling jfkeis@bu.edu
 // AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu
 //
 // w10_wordplayer.cpp
 // g++ -std=c++14 -O2 ./output2 source.cpp
 
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

// void permute(char a[], int i, int n)
// {
//    int j;
//    if (i == n)
//      cout << a << endl;
//    else
//    {
//        for (j = i; j <= n; j++)
//        {
//           swap(a[i], a[j]);          
//           permute(a, i+1, n);
//           swap(a[i], a[j]);
//        }
//    }
// }
//************ permutations ****************
	// char a[] = "ABCD";
 //  	permute(a, 0, 3);
 //  	getchar();
//******************************************


int main(int argc, char *argv[]){

	ifstream big_wordlist;
	big_wordlist.open(argv[1]);

	string word;
	vector<string> mymap;
	map<int,vector<string>> mymap;

	while (getline(big_wordlist, word)) {
		mymap[word.size()].push_back(word);
	}

	// while (getline(big_wordlist, word)) 
	// {
	// 	mymap.push_back(word);
	// }
	// cout << mymap[2] << endl;
	
	big_wordlist.close();

	// vector<string> a = mymap.at(2);
	// for (int i; i < a.size(); i++){
	// 	cout << a[i] << endl;	
	// }
	
	// map<int,vector<string>> mymap = {
 //                { 10, {"lambda","alpha"} },
 //                { 20, {"theta","beta"} },
 //                { 30, {"phi","gamma"} } };

 //  	mymap.at(10) = {"alpha","lambda"};
 //  	mymap.at(20) = {"beta","theta"};
 //  	mymap.at(30) = {"gamma","phi"};

  	// for (auto& x: mymap) {
   //  	cout << x.first << '\n';
   //  	 // << ": " << x.second
  	// }

	// for(int i = 1; i < 3; i++){
	// 	cout << mymap[i] << endl;
	// }
	

	// sort( big_wordlist.begin(), big_wordlist.end());

	// // for(int i = 0; i < big_wordlist.size(); i++){
	// // 	cout << i << endl;
	// // }

	return 0;
}