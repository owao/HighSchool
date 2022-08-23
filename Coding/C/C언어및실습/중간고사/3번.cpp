#include <stdio.h>
#include <stdlib.h>

int sumWithReverse(int n){
	int sum = n;
	int reverseN;
	int k = 10; //임시 변수
	int a = 1; //자릿수 카운트 
	int p = 1;
	
	while(true){ //자릿수 카운트 
		if(k>n){
			break;
		}
		a += 1;
		k = k*10; 
	}
	
	for(int i=1; i<a+1; i++){
		for(int j=a; j>i; j--){
			p = p*10;
		}
		reverseN += (n%10)*p;
		
		n= n/10;
		p=1;
	}
	
	sum += reverseN;
	return sum;
}

int main(int argc, char *argv[]) {
	
	int n;
	int sum;
	
	scanf("%d", &n);
	sum = sumWithReverse(n);
	printf("%d",sum);
	
	return 0;
}
