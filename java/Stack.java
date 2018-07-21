class Stack{

	private int size;
	private int top;
	int[] data;
	
	Stack(int size){

		this.size = size;
		data = new int[size];
		top = -1;
	}

	public void push(int item) throws CustomException{

		if(!isFull()){
			data[++top] = item;
		}
		else{
			throw new CustomException("Stack Overflow");
		}
	}

	public boolean isEmpty(){

		return top == -1;

	}

	public boolean isFull(){

		return top == size;
	}

	public int pop() throws CustomException{

		if(!isEmpty()){
			return data[top--];
		}
		else{
			throw new CustomException("Stack empty");
		}
	}


	public static void main(String[] args) {

		Stack s = new Stack(4);
		s.push(3);
		s.push(5);
		s.push(1);
		System.out.println(s.pop());
		System.out.println(s.pop());
		System.out.println(s.pop());
		System.out.println(s.pop());
		System.out.println(s.pop());
		System.out.println(s.pop());
	}
}

https://acm.ultimatix.net/svn/Ultimatix_GlobalApps/Dev_branch/TCS_Ultimatix_ApplyAndInitiate/CR_7275377/Source_Code/Android/InitiateApply
https://acm.ultimatix.net/svn/Ultimatix_GlobalApps/Dev_branch/TCS_Ultimatix_ApplyAndInitiate/CR_7275377/Source_Code/Android 