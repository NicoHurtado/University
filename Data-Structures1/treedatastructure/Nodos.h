#include <iostream>
using namespace std;

class NodoPag{
    public:
    string valor;
    NodoPag *izq = NULL;
    NodoPag *der = NULL;
    NodoPag(string pag){
        this->valor = pag;
    }
};

class NodoSubTerm{
    public:
    string valor;
    NodoSubTerm *izq = NULL;
    NodoSubTerm *der = NULL;
    NodoPag *pag = NULL;
    NodoSubTerm(string subterm){
        this->valor = subterm;
    }
};

class NodoTerm{
    public:
    string valor;
    NodoTerm *izq = NULL;
    NodoTerm *der = NULL;
    NodoPag *pag = NULL;
    NodoSubTerm *subterm = NULL;
    NodoTerm(string term){
        this->valor = term;
    }
};