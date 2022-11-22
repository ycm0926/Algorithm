import java.util.Scanner;

public class Main { 
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
				
		int N1 = sc.nextInt();
		int ten,one,sum;
		int cnt = 0,N2 = 0;
		
		N2=N1;
		
		do {
			
			ten = (N2/10);
			one = (N2%10);
			sum = ((ten+one)%10);
			N2 = ((10*one)+sum);			
			
			cnt++;
		
		}while(N1!=N2);
		
		System.out.println(cnt);
	}	
}