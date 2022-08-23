#include <stdio.h>

int main(){
	
	int N;
	int even, odd;

	scanf("%d", &N);
	
	for(int i=1; i<N+1; i++){
		if(i%2==0){
			even += i;
		}
		else{
			odd += i;
		}
	}
	
	printf("%d\n%d", even, odd-1);

}
