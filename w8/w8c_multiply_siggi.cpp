
#include <vector>
#include <iostream>
#include <fstream>	
#include <string>

using namespace std;

// typedef vector< vector<int> > int_matrix;

// int_matrix multply(const & int_matrix A,const & int_matrix B){

//  int M = A.size();
//  int K = A[0].size();
//  int L = B[0].size();

//  int_matrix c(M,L);
 
//  for (int i=0;i<M;i++)
//     for (int j=0;j<L;j++)
//         for (int n=0;n<N;n++)
//             c[i][j] = A[i][n]*B[n][j]


// }


int main(int argc, char const *argv[])
{
	ifstream thisfile1, thisfile2; // note: this is an IFSTREAM, "I" stands for INPUT

	int one,two,three,four;
	vector<int> squares;       
    
	thisfile1.open(argv[1]);
	thisfile2.open(argv[2]);

	while (thisfile1 >> one >> two >> three >> four)
	{ 
		cout << one << " " << two << " " << three << " " << four << endl;
		//squares.push_back(two);
    }
	
	while (thisfile2 >> one >> two >> three >> four)
	{ 
		cout << one << " " << two << " " << three << " " << four << endl;
		//squares.push_back(two);
    }    

    thisfile1.close();
    thisfile2.close();

	

	ofstream filewithmatrix3;

	filewithmatrix3.open("file3.txt");

	for (int i=1; i <= 10; i++)
       filewithmatrix3 << i << " " << i*i << endl;

    filewithmatrix3.close();


  


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