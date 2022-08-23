#include <stdio.h>

int main(){
	
	float x;
	float y;
	int quadrant;
	
	scanf("%f %f", &x, &y);
	
	(x>0) ? ((y>0) ? (quadrant = 1) : (quadrant = 4)) : ((y<0) ? (quadrant = 3) : (quadrant = 2));
	
	printf("%d»çºÐ¸é", quadrant);
		
}
