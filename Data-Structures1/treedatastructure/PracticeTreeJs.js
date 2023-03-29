class node{
    constructor(data){
    this.data = data
    this.left = null
    this.right = null
    }
    
}

class tree{
    constructor(){
        this.root = null
    }
    
    add(root, data){
        if(root == null){
            let NewOne = new node(data)
            return NewOne
        }
        else{
            if(data < root.data){
                root.left = this.add(root.left, data)
            }
            else{
                root.right = this.add(root.right, data)
            }
            return root
        }
    }

    put(data){
        this.root = this.add(this.root, data)
    }

    show(root){
        if(root == null){
            return;
        }
        else{
            this.show(root.left)
            console.log(", " + root.data)
            this.show(root.right)
        }
    }

    showTree(){
        this.show(this.root)
    }

}

//function main(){
let Tree = new tree()
Tree.put(5)
Tree.put(4)
Tree.put(7)
Tree.put(2)
Tree.put(9)
Tree.showTree()
//}   


