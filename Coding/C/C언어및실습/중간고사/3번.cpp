#include <stdio.h>
#include <stdlib.h>

int sumWithReverse(int n){
	int sum = n;
	int reverseN;
	int k = 10; //�ӽ� ����
	int a = 1; //�ڸ��� ī��Ʈ 
	int p = 1;
	
	while(true){ //�ڸ��� ī��Ʈ 
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
