
#include <vector>
#include <iostream>
#include <fstream>	
#include <string>

using namespace std;
int main(int argc, char const *argv[])
{

	ifstream thisfile; // note: this is an IFSTREAM, "I" stands for INPUT

	int one,two;
	vector<int> squares;       
    

	thisfile.open("argv[1]");

	while (thisfile >> one >> two)
	{ 
		cout << one << " " << two << endl;
		squares.push_back(two);
    }

    thisfile.close(); 

    for (auto s: squares){
    	cout << s << endl;
    }

	// ofstream filewithmatrix3;

	// filewithmatrix3.open("file3.txt");

	// for (int i=1; i <= 10; i++)
 //       filewithmatrix3 << i << " " << i*i << endl;

 //    filewithmatrix3.close();


  return 0;


    // for (int i=1; i<argc ; i++)
    // {    
    //     cout << i << " ";
    //     try 
    //     {
    //         double v = stod(argv[i]);  
    //         cout << v << endl;
    //         continue;
    //     }
    //     catch (...)
    //     {
    //         cout << argv[i] << " is not a double.";
    //     }
    //     cout << endl;
    // }
}