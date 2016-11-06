// AUTHOR johnkeisling jfkeis@bu.edu
// AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu
//
// w8c_muliply.cpp
// g++ -std=c++14 -O2 ./output2 source.cpp

#include <iostream>
#include <fstream>
#include <vector>
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

int main(){
    
    string line;
    ofstream myfile1;
    ofstream myfile2;
    ifstream myRfile1;
    ifstream myRfile2;
    myfile1.open ("xtest3.txt");
    myfile2.open ("xtest4.txt");
    myRfile1.open("xtest1.txt");
    myRfile2.open("xtest2.txt");
    
    /*
     freopen("xtest1.txt", "rb", stdin);
     while(getline(cin, line)){
     myfile1 << line << endl;
     cout << line << endl;
     }
     myfile1.close();
     */
    
    
    vector<vector<int>> data1;
    vector<vector<int>> data2;
    
    /*
     int M = int(data1.size());
     int N = int(data1[0].size());
     int L = int(data2.size());
     
     cout << M;
     */
    
    //while (!myRfile1.eof()) {
    for(int i = 0; i < 3; i++){  //row
        vector<int> tmpVec;
        int tmpString;
        
        for (int j = 0; j < 4; j++){  //col
            myRfile1  >> tmpString;
            myfile1 << tmpString << " ";
            tmpVec.push_back(tmpString);
        }
        data1.push_back(tmpVec);
        myfile1 << endl;
    }
    //}
    myfile1.close();
    
    //while (!myRfile2.eof()) {
    for(int i = 0; i < 4; i++){ //row
        vector<int> tmpVec;
        int tmpString;
        
        for (int j = 0; j < 3; j++){  //col
            myRfile2  >> tmpString;
            myfile2 << tmpString << " ";
            tmpVec.push_back(tmpString);
        }
        data2.push_back(tmpVec);
        myfile2 << endl;
    }
    //}
    myfile2.close();
    
    int rows = int(data1.size());
    int cols = int(data2[0].size());
    cout << rows << "\n";
    cout << cols << "\n";
    multMatI(4, cols, data1, data2);
    
    
    
    cout << data1[2][3] << "\n";
    cout << data2[3][2] << "\n";
    
    
    cout << "fin";
    return 0;
}

/*
 main(int argc, char *argv[])
 file1.open(argv[1])
 file2.open(argv[2])
 */

