#include <stdio.h>

int main(){	

	int k;
	scanf("%d", &k);
	
	for(int i=1; i<k+1; i++){  //행 
		if(i == k/2 +1){ //정가운데 줄(x측) 
			for(int j=1; j<k+1; j++){ //열 
				if(j ==  k/2 +1){ //원점 
					printf("0");
				}
				else{
					printf("+");
				}
			}
		}
		else{
			for(int j=1; j<k+1; j++){
				if(i == k/2 +1){  // y축 
					printf("I");
				}
				else if(i+j == k+1){  //그래프 
					printf("*");
				}
				else{
					printf(".");
				}			
			}
		} 
		printf("\n");
	}
}
