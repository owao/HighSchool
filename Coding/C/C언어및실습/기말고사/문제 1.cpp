#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	int a, b, c;
	scanf("%d %d\n", &a, &b);
	int arr1[5], arr2[5];
	int i=0;
	int sum=0;
	
	while(a!=0){
		c=a%10;
		arr1[i]=c;
		a=a/10;
		i++;
	}
	
	i=0;
	while(b!=0){
		c=b%10;
		arr2[i]=c;
		b=b/10;
		i++;
	}
	
	for(int i=0; i<5; i++){
		for(int j=0; j<5; j++){
			sum+=arr1[i]*arr2[j];
		}
	}
	
	printf("%d", sum);

}
