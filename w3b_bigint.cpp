//
//  main.cpp
//  w3a_bigint.cpp
//
// AUTHOR John Keisling jfkeis@bu.edu
// AUTHOR Sigurdur Thorvaldsson sigurdur@bu.edu
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef vector<int> Poly;

typedef string BigInt;

// Add two polynomials, returning the result
Poly add_poly(const Poly &a,const Poly &b)
{
    // declare temporary vectors
    Poly funca = a;
    Poly funcb = b;
    
    // append zeroes to front
    while(funca.size() > funcb.size())
    {
        funcb.insert(funcb.begin() , 0);
    }
    
    while(funcb.size() > funca.size())
    {
        funca.insert(funca.begin() , 0);
    }
    
    // intialize sum vector
    Poly sum(funca.size());
    
    for (int i = 0; i < funca.size(); i++) {
        sum[i] = funca[i] + funcb[i];
    }
    
    return sum;
}

// Multiply two polynomials, returning the result.
Poly multiply_poly(const Poly &a,const Poly &b)
{
    Poly sum(a.size()+b.size()-1);
    int place = 0;
    for (int i = (int)a.size() - 1; i >= 0; i--)
    {
        Poly temp(b.size());
        for (int j = 0; j < b.size(); j++)
        {
            temp[j] = a[i] * b[j];
        }
        for (int k = 0; k < place; k++)
        {
            temp.push_back(0);
        }
        
        sum = add_poly(sum,temp);
        
        place++;
    }
    return sum;
}

BigInt multiply_int(const BigInt &a,const BigInt &b)
{
    int lena = (int) a.size();
    Poly A(lena,0);
    for(int i = 0; i < a.size(); i++)
    {
        // converting char to int returns the ascii value. int 0 is 48 in ascii.
        A[i] = (int)a.at(i) - 48;
    }
    int lenb = (int) b.size();
    Poly B(lenb);
    for(int i = 0; i < b.size(); i++)
    {
        // converting char to int returns the ascii value. int 0 is 48 in ascii.
        B[i] = (int)b.at(i) - 48;
    }
    Poly Prod = multiply_poly(A, B);
    BigInt product;
    for(int i = 0; i < Prod.size(); i++)
    {
        product = product.append(to_string(Prod[i]));
    }
    return product;
}



int main()
{
    
    BigInt A,B;
    
    //cin >> A >> B;
    A = "111111";
    B = "1111111";
    
    
    cout << multiply_int(A,B) << endl;
    
}
