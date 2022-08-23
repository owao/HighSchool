#include <stdio.h>

int main(){
	
	int a, b;
	int square, hexa;
	
	scanf("%d %d", &a, &b);
	
	for(int i=a+1; i>0; i--){
		square += i;
	}
	
	for(int i=1; i<b; i++){
		hexa += 6*i;
	}
	
	printf("%d %d", square+1, hexa);

}
