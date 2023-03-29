#include <iostream>
#include <string>
using namespace std;

struct node{

    int data;
    node* left;
    node* right;

    node(int n){
        data = n;
        left = NULL;
        right = NULL;
    }

};

class Tree{
    
    public:

    node* raiz = NULL;

    void add(node* &root, int n){
        if (root == NULL){  
            node* NewOne = new node(n);
            root = NewOne;
        }   
        
        else{
            if(root->data > n){
                add(root->left, n);
            }
            else{   
                add(root->right, n);
            }
        }
        
    }

    void Put(int n){
        add(raiz, n);
    }

    void show(node* root){
        if (root == NULL){
            return;
        }
        else{
            show(root->left);
            cout <<root->data<<", ";
            show(root->right);
        }
    }


    void showTree(){
        show(raiz);
        
    }

};

int main(){
    Tree* NewTree = new Tree();
    
    
    NewTree->Put(3);
    NewTree->Put(6);
    NewTree->Put(1);
    NewTree->Put(4);
    NewTree->Put(7);

    
    NewTree->showTree();
    

    return 0;
}