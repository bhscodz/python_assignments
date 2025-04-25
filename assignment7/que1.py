class Linked_list:
    Head=None
    total_node=0
    def __init__(self,val,init=False):
        if(init):
            return
        Linked_list.total_node+=1
        if(self.Head==None):
            Linked_list.Head=self
            self.val=val
            self.next=None
        else:
            self.val=val
            self.next=None
            temp=Linked_list.Head
            while(temp.next!=None):
                temp=self.next
            temp.next=self
    @staticmethod
    def add_node(val):
        Linked_list(val)
    @staticmethod
    def display():
        temp=Linked_list.Head
        while(temp!=None):
            print(temp.value)
            temp=temp.next
    @staticmethod
    def delete_node(index):
        if(index>=Linked_list.total_node):
            print("index out of range")
        else:
            temp=Linked_list.Head
            while(index>1):
                temp_prev=temp
                temp=temp.next
                index-=1
            temp_prev.next=temp.next

            
ll=Linked_list
while(True):
    a=int(input("enter 1.to add new node\n2.to display linked list\n3.to delete a node at a particular index\n4.to exit"))
    if(a==4):
        break
    if(a==1):
        ll.add_node(int(input("enter the value")))
    if(a==2):
        ll.display()
    if(a==3):
        ll.delete_node(int(input("enter the index of node to be deleted")))

        
