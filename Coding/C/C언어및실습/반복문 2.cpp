#include <stdio.h>

int main(){	

	int k;
	scanf("%d", &k);
	
	for(int i=1; i<k+1; i++){  //�� 
		if(i == k/2 +1){ //����� ��(x��) 
			for(int j=1; j<k+1; j++){ //�� 
				if(j ==  k/2 +1){ //���� 
					printf("0");
				}
				else{
					printf("+");
				}
			}
		}
		else{
			for(int j=1; j<k+1; j++){
				if(i == k/2 +1){  // y�� 
					printf("I");
				}
				else if(i+j == k+1){  //�׷��� 
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
