#include <stdio.h>

int main(){
	
	int h;
	int m;
	int s;
	
	printf("Enter hour min sec:");
	scanf("%d %d %d", &h, &m, &s);
	
	if (0<=h and 12>h)
		printf("\n오전 %.2d:%.2d:%.2d", h, m, s);
	if (12<=h and 24>h){
		h=h-12;
		printf("\n오후 %.2d:%.2d:%.2d", h, m, s);		
	}
		
}
