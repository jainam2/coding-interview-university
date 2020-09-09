class ArrayQueue{
	private int size;
	private int capacity;
	private int front = 0;
	private int rear = 0;
	private int queue[];

	ArrayQueue(int c){
		capacity = c;
		queue = new int[c];
	}

	ArrayQueue(){
		capacity = 8;
		queue = new int[8];
	}


	public void enqueue(int val){
		if (queue[front] == 0){
			queue[front] = val;
			front = (front + 1) % capacity;
			size++;
			System.out.println("Element added: " + val);
		}
		else{
			System.out.println("Size is not sufficient!");
		}
	}


	public void dequeue(){
		if (queue[rear] == 0){
			System.out.println("Queue is empty!");
		}
		else{
			queue[rear] = 0;
			rear = (rear + 1) % capacity;
			size--;
		}
	}


	public void display(){

		int temp = rear;
		while (temp != front){
			System.out.print(queue[temp] + " ");
			temp = (temp + 1) % capacity;
		}
		System.out.println();
	}


	public static void main(String[] args){
		// Test the object here.
	}
}