#include <iostream>
#include <string>
using namespace std;

class node{
    
    public:
    int data;
    node* next;

    node(int n){
        data = n;
        next = NULL;
    }
    
};
    

class linkedList{

    public:
    node* head = NULL;
    
    void add(int n){
        if(head == NULL){
            head = new node(n);
        }
        else{
            node* current = head;
            while (current->next != NULL){
                current = current->next;
            }
            current->next = new node(n);
        }
    }

    void show(){
        node* current = head;
        while (current != NULL){
            cout << current->data << "->";
            current = current->next;
        }
        
    }

    
};

int main(){

    linkedList* NewList = new linkedList();

    NewList->add(1);
    NewList->add(2);
    NewList->add(3);

    NewList->show();
}