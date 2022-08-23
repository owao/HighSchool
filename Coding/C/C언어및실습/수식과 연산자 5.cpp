#include <stdio.h>
#define PI 3.14

int main(){
	
	float r;
	float outer_area;
	float volume;
	
	scanf("%f", &r);
	
	outer_area = 4*PI*r*r;
	volume = (4*PI*r*r*r)/3;
	
	printf("%f %f", outer_area, volume);
	
}
