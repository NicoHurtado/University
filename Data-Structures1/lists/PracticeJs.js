class node{
    constructor(data){
        this.data = data
        this.next = null
    }
}
class list{
    constructor(){
        this.head = null
    }

    add(dato){
        if (this.head == null){
            let NewOne = new node(dato)
            this.head = NewOne
        }
        else {
            let current = this.head
            while(current.next != null){
                current = current.next
            }
            let NewOne = new node(dato)
            current.next = NewOne
        }
    }

    show(){
        let current = this.head
        while(current != null){
            //console.log(current.data)
            process.stdout.write(current.data + "->")
            current = current.next
        }
    }
}

function main(){
    let NewList = new list()
    NewList.add(4)
    NewList.add(5)
    NewList.add(7)
    NewList.add(3)
    NewList.add(18)

    NewList.show()
    
    console.log(NewList.head.data)
    
}

main()