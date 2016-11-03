
 // AUTHOR johnkeisling jfkeis@bu.edu
 // AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu
 //
 // w8c_muliply.cpp
 // g++ -std=c++14 -O2 ./output2 source.cpp
 
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

//w8c_multiply dtype M N L file1 file2 file3

/*
void multMatD(int i, int j, vector<vector<double>> mat1, vector<vector<double>> mat2) {
    
    vector<vector<double>> mat3;
    for (int r = 0; r < i; r++) {
        for (int c = 0; c < j; c++) {
            for (int in = 0; in < i; in++) {
                mat3[r][c] += mat1[r][in] * mat2[in][c];
            }
            cout << mat3[r][c] << "  ";
        }
        cout << "\n";
    }
}
*/
template <typename T>
T multMatI(int i, int j, T mat1, T mat2) {
    
    vector<int> v(i, 0);
    vector<vector<int> > mat3(j,v);
    for (int r = 0; r < i-1; r++) {  //added -1 to fix
        for (int c = 0; c < j; c++) {
            for (int in = 0; in < i; in++) {
                mat3[r][c] += mat1[r][in] * mat2[in][c];
            }
            cout << mat3[r][c] << "  ";
        }
        cout << "\n";
    }
    return mat3;
}

 int main(int argc, char *argv[]){
     
     /*
     for(int i=0; i<argc; i++){
         if(argc != 6 || argc != 8){
             return 1;
         }
         //if(argv[i]
     }
      */
     
     ifstream file1, file2;
     ofstream file3;
     //file1.open(argv[1]);
     //file2.open(argv[2]);
     //file3.open(argv[3]);
     file1.open("xtest1.txt");
     file2.open("xtest2.txt");
     file3.open("xtest3.txt");
     int m = 3;
     int n = 4;
     int l = 3;
     
     
     vector<vector<int>> data1;
     vector<vector<int>> data2;
     
     //while (!myRfile1.eof()) {
         for(int i = 0; i < m; i++){  //row
             vector<int> tmpVec;
             int tmpString;
             
             for (int j = 0; j < n; j++){  //col
                 file1  >> tmpString;
                 //myfile1 << tmpString << " ";
                 tmpVec.push_back(tmpString);
             }
             data1.push_back(tmpVec);
             //myfile1 << endl;
         }
     //}
     file1.close();
     
     //while (!myRfile2.eof()) {
         for(int i = 0; i < n; i++){ //row
             vector<int> tmpVec;
             int tmpString;
             
             for (int j = 0; j < l; j++){  //col
                 file2  >> tmpString;
                 //myfile2 << tmpString << " ";
                 tmpVec.push_back(tmpString);
             }
             data2.push_back(tmpVec);
             //myfile2 << endl;
         }
     //}
     file2.close();
     
     int M = int(data1.size());
     //int N = int(data1[0].size());
     int L = int(data2[0].size());

     vector<vector<int>> result = multMatI(M+1, L, data1, data2);
     
     for(int i = 0; i < M; i++){ //row
         vector<int> tmpVec;
         for (int j = 0; j < L; j++){  //col
             file3 << result[i][j] << " ";
         }
         file3 << endl;
     }
     cout << "got here";
     file3.close();
     cout << "and here ";
     
     //cout << "fin ";
     return 0;
 }

//exit(1)
