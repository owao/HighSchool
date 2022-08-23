#include <stdio.h>
#include <stdlib.h>

void checkChar(){
	
	char c;
	while(true){
		scanf(" %c", &c);
		if(c=='q'){
			return;
		}
		else if (c>='a' && c <='z'){
			printf("Lowercase \n");
		}
		else if (c>='A' && c<='Z'){
			printf("Uppercase \n");
		}
		else{
			printf("Etc\n");
		}
	}
}

int main(int argc, char *argv[]){
	
	checkChar();
	
}
