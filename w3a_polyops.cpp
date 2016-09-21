//
//  main.cpp
//  w3a_polyops.cpp
//
// AUTHOR John Keisling jfkeis@bu.edu
// AUTHOR Sigurdur Thorvaldsson sigurdur@bu.edu
//

#include <iostream>
#include <vector>
using namespace std;

typedef vector<double> Poly;

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
        cout << sum[i] << " ";
    }
    
    return sum;
}

// Multiply two polynomials, returning the result.
Poly multiply_poly(const Poly &a,const Poly &b)
{
    Poly sum(a.size()+b.size()-1);
    for (int i = a.size() - 1; i >= 0; i--)
    {
        
        
        for (int j = 0; j < b.size(); j++)
        {
            a[i] * b[j]
        }
    }
    
    
}




int main() {
    Poly ina;
    Poly inb;
    // cout << "Polynomial A: ";
    // cin >> A
    // cout << "Polynomial B: ";
    // cin >> B
    ina = {3,4,5,6,7};
    inb = {2,5,1};
    add_poly(ina, inb);
    
    return 0;
}
