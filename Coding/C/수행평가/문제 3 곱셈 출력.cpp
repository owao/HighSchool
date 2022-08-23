#include <stdio.h>

int main(){
	
	int n;
	int m;
	
	int end;
	int i;
	int u;
	int s;
	
	printf("Enter n m:");
	scanf("%d %d", &n, &m);
	for (i=1; i<n+1; i++){
		u=m*i;
		for (s=m; s>0; s--){
			printf("%6d", u);
			u=u-1;
		}
		printf("\n");			
	}
		
}
