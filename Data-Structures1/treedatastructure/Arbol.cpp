#include <iostream>
#include <stdlib.h>
#include <cstdlib>
#include <fstream>
#include "Nodos.h"
using namespace std;

void insertarPag(NodoPag *&pag, string valor) {
    if (pag == NULL) {
        NodoPag *nuevo = new NodoPag(valor);
        pag = nuevo;
    } else {
        string pagValor = pag->valor;
        if (valor <= pagValor) {
            insertarPag(pag->izq, valor);
        } else {
            insertarPag(pag->der, valor);
        }
    }
}

void insertarSubTerm(NodoSubTerm *&subterm, string valor) {
    if (subterm == NULL) {
        NodoSubTerm *nuevo = new NodoSubTerm(valor);
        subterm = nuevo;
    } else {
        string subtermValor = subterm->valor;
        if (valor <= subtermValor) {
            insertarSubTerm(subterm->izq, valor);
        } else {
            insertarSubTerm(subterm->der, valor);
        }
    }
}

void insertarTerm(NodoTerm *&term, string valor) {
    if (term == NULL) {
        NodoTerm *nuevo = new NodoTerm(valor);
        term = nuevo;
    } else {
        string termValor = term->valor;
        if (valor <= termValor) {
            insertarTerm(term->izq, valor);
        } else {
            insertarTerm(term->der, valor);
        }
    }
}

void recorrerPag(NodoPag *pag) {
    if (pag == NULL) {
        return;
    } else {
        recorrerPag(pag->izq);
        cout << ", " << pag->valor;
        recorrerPag(pag->der);
    }
}

void recorrerSubTerm(NodoSubTerm *subterm) {
    if (subterm == NULL) {
        return;
    } else {
        recorrerSubTerm(subterm->izq);
        cout << "--Subtermino-- : "+subterm->valor;
        recorrerPag(subterm->pag);
        cout << endl;
        recorrerSubTerm(subterm->der);
    }
}

void recorrerTerm(NodoTerm *term) {
    if (term == NULL) {
        return;
    } else {
        recorrerTerm(term->izq);
        cout << "TERMINO: " + term->valor;
        recorrerPag(term->pag);
        cout << endl;
        recorrerSubTerm(term->subterm);
        recorrerTerm(term->der);
    }
}
/*--------------------------------------------------------------------*/


string ExtraerPalabra(string palabra){
    int primerNumero = palabra.find_first_of("0123456789");
    string palabraFinal = palabra.substr(1, primerNumero-1);
    return palabraFinal;
}

void ExtraerPag(NodoPag *&Apag, string palabra){
    int primerNumero = palabra.find_first_of("0123456789");
    int NumeroPaginas= atoi(palabra.substr(primerNumero, 1).c_str());
    int Num_Uno = palabra.find_first_of("0123456789");
    for(int i=0; i<NumeroPaginas; i++){
        string pag = palabra.substr(Num_Uno+1, 2);
        insertarPag(Apag, pag);
        Num_Uno+=2;
    }
}

NodoTerm* InsertarEnNodo(NodoTerm *&term, string valor){
    if(term == NULL){
        return NULL;
    }else{
        string termValor = term->valor;
        if(valor == termValor){
            return term;
        }else if(valor < termValor){
            return InsertarEnNodo(term->izq, valor);
        }else{
            return InsertarEnNodo(term->der, valor);
        }
    }
}

NodoSubTerm* InsertarEnNodoSub(NodoSubTerm* subterm, string valor){
    if(subterm == NULL){
        return NULL;
    }else if(subterm->valor == valor){
        return subterm;
    }else if(valor < subterm->valor){
        return InsertarEnNodoSub(subterm->izq, valor);
    }else{
        return InsertarEnNodoSub(subterm->der, valor);
    }
}


void lectura(){
    ifstream archivo;
    archivo.open("entrada.txt", ios::in);
    if(archivo.fail()){
        cout << "No se pudo abrir el archivo";
        exit(1);
    }
    string linea;

    string lineaCompleta;
    string SoloPalabra;
    NodoTerm* raizTerm = NULL;
    NodoTerm* TerminoPrincipalIngresado = NULL;

    while(!archivo.eof()){
        getline(archivo, linea);
        lineaCompleta = linea;
        if(lineaCompleta[0] == 'M'){
            SoloPalabra = ExtraerPalabra(lineaCompleta);
            insertarTerm(raizTerm, SoloPalabra);
            TerminoPrincipalIngresado = InsertarEnNodo(raizTerm, SoloPalabra);
            ExtraerPag(TerminoPrincipalIngresado->pag, lineaCompleta);
        } else if(lineaCompleta[0] == 'S'){
            SoloPalabra = ExtraerPalabra(lineaCompleta);
            insertarSubTerm(TerminoPrincipalIngresado->subterm, SoloPalabra);
            ExtraerPag(InsertarEnNodoSub(TerminoPrincipalIngresado->subterm,SoloPalabra)->pag, lineaCompleta);
        }
    }
    archivo.close();
    recorrerTerm(raizTerm);
}

int main(){
    lectura();
    return 0;

}
