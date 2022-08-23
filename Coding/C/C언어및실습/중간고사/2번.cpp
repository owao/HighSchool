#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	
	int A;
	int B;
	int num = 0; //소수 개수
	int sum = 0; //소수 합 
	int count = 1; //임시 변수 
	
	scanf("%d %d", &A, &B);
	
	for(int i=A; i<B+1; i++){
		if(i==1 || (i>2 && i%2==0)){ //1이거나 짝수는 거른다 
			continue;
		}
		 for(int j=2; j<i; j++){ //나눠지는 수가 있는지 검사한다 
		 	if(i%j==0){
		 		count=0;
			 }
		}
		if(count){
			num += 1;
			sum += i;
		}
		count = 1; //초기화 
	}
	
	printf("%d %d", num, sum);
	
	return 0;
}
