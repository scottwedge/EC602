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

void permute(char a[], int i, int n)
{
   int j;
   if (i == n)
     cout << a << endl;
   else
   {
       for (j = i; j <= n; j++)
       {
          swap(a[i], a[j]);          
          permute(a, i+1, n);
          swap(a[i], a[j]);
       }
   }
}


int main(int argc, char *argv[]){
	char a[] = "ABCD";
  	permute(a, 0, 3);
  	getchar();
	return 0;
	// ifstream big_wordlist;

	// map<int, vector<string>> mymap;
	// mymap[1] = ['Siggi'];
	// //mymap[2] = "John";

	// for(int i = 1; i < 3; i++){
	// 	cout << mymap[i] << endl;
	// }
	// big_wordlist.open(argv[1]);

	// sort( big_wordlist.begin(), big_wordlist.end());

	// // for(int i = 0; i < big_wordlist.size(); i++){
	// // 	cout << i << endl;
	// // }

	// big_wordlist.close();
}