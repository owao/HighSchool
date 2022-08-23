#include <stdio.h>
#include <stdlib.h>

int countOfTiles(int n){
	int result;
	int i=1; //임시 변수 
	
	while(true){
		if(i*i>n){
			break;
		}
		if(i%2){
			result = i;
		}
		else{
			result = -i;
		}
		i += 1;		
	}
	
	return result;
}

int main(int argc, char *argv[]) {

	int tiles;
	int result;
	
	scanf("%d", &tiles);
	result = countOfTiles(tiles);
	printf("%d",result);
	
	return 0;
}
