
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

template <typename T>
T multMatI(int i, int j, T mat1, T mat2) {
    
    vector<double> v(i, 0);
    T mat3(j,v);
    for (int r = 0; r < i-1; r++) {  //added -1 to fix
        for (int c = 0; c < j; c++) {
            for (int in = 0; in < i; in++) {
                mat3[r][c] += mat1[r][in] * mat2[in][c];
            }
            //cout << mat3[r][c] << "  ";
        }
        //cout << "\n";
    }
    return mat3;
}

bool is_file_exist(const char *fileName)
{
    std::ifstream infile(fileName);
    return infile.good();
}

int main(int argc, char *argv[]){
     
     int m;
     int n;
     int l;
     ifstream file1, file2;
     ofstream file3;
     bool f1Check;
     bool f2Check;
     bool f3Check;

     if(argc==8){
         file1.open(argv[5]);
         file2.open(argv[6]);
         file3.open(argv[7]);
         m = atoi(argv[2]);
         n = atoi(argv[3]);
         l = atoi(argv[4]);
         f1Check = is_file_exist(argv[5]);
         f2Check = is_file_exist(argv[6]);

     }
     else if(argc==6){
         file1.open(argv[3]);
         file2.open(argv[4]);
         file3.open(argv[5]);
         m = atoi(argv[2]);
         n = m;
         l = m;
         f1Check = is_file_exist(argv[3]);
         f2Check = is_file_exist(argv[4]);
     }
     else{
         // if arguments invalid
         return 1;
     }
    
    if(m <= 0 || n <=0 || l <= 0){
        return 2;
    }
    
     //check that files exist
     if(f1Check == false){
         return 2;
     }
     if(f2Check == false){
         return 2;
     }
     
     string dtype = argv[1];
    
     //file1.open("xtest1.txt");
     //file2.open("xtest2.txt");
     //file3.open("xtest3.txt");
     //bool dtype = true;
     
     //int m = 3;
     //int n = 4;
     //int l = 3;
     
     /*
     if(dtype){
        vector<vector<int>> data1;
        vector<vector<int>> data2;
        cout << "this  ";
     }
     else if (!dtype){
         vector<vector<double>> data1;
         vector<vector<double>> data2;
     }
      */
     
     vector<vector<double>> data1;
     vector<vector<double>> data2;

     //while (!myRfile1.eof()) {
         for(int i = 0; i < m; i++){  //row
             vector<double> tmpVec;
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
             vector<double> tmpVec;
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
     int N = int(data1[0].size());
     int L = int(data2[0].size());
    
     if(m != M || n != N || l != L){
         return 3;
     }
     if(m != l)
     {
         return 3;
     }
    
     vector<vector<double>> result = multMatI(M+1, L, data1, data2);
     vector<vector<double>> resultInt;
     resultInt.reserve(result.size());
     
     if(dtype == "int")
     {
         for (const auto& elem : result) {
             resultInt.emplace_back(elem.begin(), elem.end());
         }
     }
    
    // check to see if file is written
    if(argc==8){
        f3Check = is_file_exist(argv[7]);
    }
    else if(argc==6){
        f3Check = is_file_exist(argv[5]);
    }
    
    if(dtype == "int"){
        for(int i = 0; i < M; i++){ //row
            vector<int> tmpVec;
            for (int j = 0; j < L; j++){  //col
                file3 << resultInt[i][j] << " ";
            }
            file3 << endl;
        }
        file3.close();
    }
    else if(dtype == "double"){
        for(int i = 0; i < M; i++){ //row
            vector<double> tmpVec;
            for (int j = 0; j < L; j++){  //col
                file3 << (double)result[i][j] << " ";
            }
            file3 << endl;
        }
        file3.close();
    }
    else{
        return 1;
    }
     
     //cout << "fin ";
     return 0;
 }

//  exit(1)
//  g++ -std=c++14 main.cpp
//  ./a.out xtest1.txt xtest2.txt xtest3.txt
