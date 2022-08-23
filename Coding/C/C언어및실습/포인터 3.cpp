#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void convert(float *grades, float *scores){
	for(int i=0; i<10; i++){
		scores[i] = grades[i]*100.0 / 4.5;
		printf("%.2f ", scores[i]);
	}
}

int main(){
	
	float grades[10] = {0};
	float scores[10] = {0};
	
	//·£´ý °ª ÀúÀå 
	srand(time(NULL));
	for(int i=0; i<10; i++){
		grades[i] = rand() % 4 +1;
		grades[i] += rand() % 100 / 100.0;
	}
	
	for(int i=0; i<10; i++){
		printf("%.2f ", grades[i]);
	}
	printf("\n"); 
	
	convert(grades, scores);
}
