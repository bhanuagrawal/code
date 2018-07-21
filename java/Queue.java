class Queue{

	private int[] data;
	private int size;
	private int head, tail;

	Queue(int size){
		this.size = size;
		head = -1;
		tail = -1;
		data = new int[size];
	}

	public void enqueue(int item) throws CustomException{


		if(head == (tail+1)%size){
    		throw new CustomException("Queue is full");
    	}
		else if(tail  == -1){
			head = 0;
			tail = 0;
			data[head] = item;
		}
		else{
			tail = (tail+1)%size;
			data[tail] = item;
		}

	}

	public int dequeue() throws CustomException{

		if(head == -1){
			throw new CustomException("Queue is empty");
		}

		int d = data[head];
		if(head == tail){
			
			head = -1;
			tail = -1;
		}
		else{
			head = (head+1)%size;
		}
		return d;
	}


	public static void main(String[] args) {
		Queue q = new Queue(4);
		q.enqueue(1);
		q.enqueue(2);
		q.enqueue(3);
		q.enqueue(4);

		System.out.println(q.dequeue());
		System.out.println(q.dequeue());
		System.out.println(q.dequeue());

		q.enqueue(1);
		q.enqueue(2);
		q.enqueue(3);
		System.out.println(q.dequeue());
		System.out.println(q.dequeue());
		System.out.println(q.dequeue());
		System.out.println(q.dequeue());
		System.out.println(q.dequeue());
		q.enqueue(4);
	}
}
