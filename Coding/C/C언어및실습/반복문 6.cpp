#include <stdio.h>

int main(){
	
	int N;
	int num, sum;
	
	scanf("%d", &N);
	
	for(int i=1; i<N+2; i++){
		num += i;
	}
	
	for(int i=0; i<N+1; i++){
		for(int j=0; j<i+1; j++){
			sum += j;
			sum += i;
		}
	}
	
	printf("%d\n%d", num, sum);

}
