#include <stdio.h>

int main(){
	
	int smallhouse = 18;
	int bighouse = 25;
	const float P = 3.305785; //평
	
	float smallhouse_p = smallhouse*P;
	float bighouse_p = bighouse*P;
	
	printf("18평 아파트 면적은 %f제곱미터, 25평 아파트 면적은 %f제곱미터입니다.", smallhouse_p, bighouse_p); 
	
}
