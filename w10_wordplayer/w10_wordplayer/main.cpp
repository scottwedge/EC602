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

// Program to print all combination of size r in an array of size n
int compare (const void * a, const void * b)
{  return ( *(int*)a - *(int*)b );  }

void combinationUtil(char arr[], char data[], int start, int end, int index, int r)
{
    // Current combination is ready to be printed, print it
    if (index == r)
    {
        for (int i=0; i<r; i++)
            printf("%c" ,data[i]);
        printf("\n");
        return;
    }
    
    // replace index with all possible elements. The condition
    // "end-i+1 >= r-index" makes sure that including one element
    // at index will make a combination with remaining elements
    // at remaining positions
    for (int i=start; i<=end && end-i+1 >= r-index; i++)
    {
        data[index] = arr[i];
        combinationUtil(arr, data, i+1, end, index+1, r);
        
        // Remove duplicates
        while (arr[i] == arr[i+1])
            i++;
    }
}

void printCombination(char arr[], int n, int r)
{
    // A temporary array to store all combination one by one
    char data[r];
    
    // Sort array to handle duplicates
    qsort (arr, n, sizeof(int), compare);
    
    // Print all combination using temprary array 'data[]'
    combinationUtil(arr, data, 0, n-1, 0, r);
}

int main(int argc, const char * argv[]) {
    /*
    ifstream big_wordlist;
    big_wordlist.open(argv[1]);
    */
    
    
    int x;
    string inword;
    cin >> inword >> x;
    
    cout << x << " " << inword << "\n";
    
    
    //string inword = "berdache";
    
    //char arr[inword.size()];//as 1 char space for null is also required
    //strcpy(arr, inword.c_str());

    //cout << arr << "\n";
    
    //cout << arr[0] << " " << arr[1] << "\n";
    
    char arr[] = {'a', 'b', 'c', 'd', 'e'};
    cout << arr << "\n";
    //int arr[] = {1, 2, 3, 4, 5};
    int n = int(sizeof(arr)/sizeof(arr[0]));
    int r = 3;
    printCombination(arr, n, r);
    
    return 0;
}
