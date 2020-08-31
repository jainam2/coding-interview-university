class LinkedList{
	private Node head = null;
	private int size = 0;

	public void display(){
		if (head != null){
			Node curr = head;
		
			while (curr != null){
				System.out.print(curr.data + "-->");
				curr = curr.next;
			}
			System.out.println("null");
		}
		else{
			System.out.println("No node found!");
		}
	}


	public int size(){
		return size;
	}

	public int value_at(int index){

		if (size > index){
			Node curr = head;
			while(index != 0){
				curr=curr.next;
				index-=1;
			}
			return curr.data;
		}
		return 0;
	}


	public void push_front(int value){
		Node new_node = new Node(value, null);

		if (head == null){
			head = new_node;
		}else{
			new_node.next = head;
			head = new_node;
		}
		size++;
	}


	public void pop_front(){
		if(head!=null){
			head = head.next;
			size -= 1;
		}
	}


	public void push_back(int value){
		Node new_node = new Node(value, null);

		if (head == null){
			head = new_node;
		}
		else{
			Node curr = head;

			while (curr.next != null){
				curr=curr.next;
			}
			curr.next = new_node;
		}
		size += 1;
	}


	public void pop_back(){
		if (head != null){
			Node curr = head;
			Node prev = head;
			while (curr.next != null){
				prev = curr;
				curr = curr.next;
			}
			prev.next = null;
			size -= 1;
		}
	}


	public int front(){
		if (head != null){
			return head.data;
		}
		return 0;
	}


	public int back(){
		if (head != null){
			Node curr=head;
			while (curr.next != null){
				curr=curr.next;
			}
			return curr.data;
		}
		return 0;
	}


	public void insert(int index, int value){
		if (size <= index || head == null){
			return ;
		}

		Node new_node = new Node(value, null);

		if (index==0){
			new_node.next = head;
			head = new_node;
			size++;
			return ;
		}


		Node curr = head;
		Node prev = head;

		while (index != 0){
			prev = curr;
			curr = curr.next;
			index--;
		}
		new_node.next = prev.next;	
		prev.next = new_node;
		size++;
	}


	public void erase(int index){
		if (size <= index || head == null){
			return ;
		}

		if (index == 0){
			head = head.next;
			size--;
			return ;
		}

		Node prev = head;
		Node curr = head;

		while (index != 0){
			prev = curr;
			curr = curr.next;
			index--;
		}

		prev.next = curr.next;
		size--;
	}

	public int value_n_from_end(int n){
		
		if (n<=size){
			n = size - n;
			Node curr = head;
			while (n != 0){
				curr=curr.next;
				n--;
			}
			if (curr != null){
				return curr.data;
			}
		}
		return 0;
	}


	public boolean find(int value){
		if(head == null){
			return false;
		}

		Node curr = head;
		while (curr.next != null && curr.data != value){
			curr = curr.next;
		}
		if (curr.data == value){
			return true;
		}
		return false;
	}


	public void remove_value(int value){
		if (find(value)){
			if (value == head.data){
				head = head.next;
			}
			else{
				Node prev = head;;
				Node curr = head;
				while (curr.data != value){
					prev = curr;
					curr = curr.next;
				}
				prev.next = curr.next;
			}
			size--;

		}
	}


	public void reverse(){
		Node prev = null;
		Node curr = head;
		Node temp;

		while (curr != null){
			temp = curr.next;
			curr.next = prev;
			prev = curr;
			curr = temp;
		}
		head = prev;
	}


}

class Node{
	int data;
	Node next;

	public Node(int d, Node n){
		data = d;
		next = n;
	}
}
