#include <stdio.h>
#include <stdlib.h>

int fibo(int n){
	if(n==1 || n==2){
		return 1;
	}
	else{
		return fibo(n-1)+fibo(n-2);
	}
}

int totalSalary(int n){
	int total = 0;
	int a; //�ӽ� ���� 
	for(int i=1; i<n+1; i++){
		a = fibo(i); //n������ �Ǻ���ġ ���� �˾Ƴ���
		total += a; 
	}
	return total;
}

int main(int argc, char *argv[]) {
	
	int date;
	int total;
	
	scanf("%d", &date);
	total = totalSalary(date);
	printf("%d",total);
	
	return 0;
}
