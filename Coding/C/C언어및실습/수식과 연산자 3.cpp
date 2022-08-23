#include <stdio.h>

int main(){
	
	char alphabet;
	 
	scanf("%c", &alphabet);

	int ascii = alphabet;
	
	printf("%d %d %d %d \n", ascii, ascii+1, ascii+2, ascii+3);
	printf("%c %c %c %c \n", ascii, ascii+1, ascii+2, ascii+3);	
	
}
