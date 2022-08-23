#include <stdio.h>

int main(){
	
	int a,b,c;
	
	scanf("%d %d %d", &a, &b, &c);
	
	
	//if answer is c
	if (a+b == c){
		printf("%d+%d=%d\n", a, b, c);
	}
	else if (a-b == c){
		printf("%d-%d=%d\n", a, b, c);
	}
	else if (b-a == c){
		printf("%d+%d=%d\n", b, a, c);
	}
	else if (a*b == c){
		printf("%d*%d=%d\n", a, b, c);
	}
	else if (a/b == c){
		printf("%d/%d=%d\n", a, b, c);
	}
	else if (b/a == c){
		printf("%d+%d=%d\n", b, a, c);
	}
	
	//if answer is b
	if (a+c == b){
		printf("%d+%d=%d\n", a, c, b);
	}
	else if (a-c == b){
		printf("%d-%d=%d\n", a, c, b);
	}
	else if (c-a == b){
		printf("%d+%d=%d\n", c, a, b);
	}
	else if (a*c == b){
		printf("%d*%d=%d\n", a, c, b);
	}
	else if (a/c == b){
		printf("%d/%d=%d\n", a, c, b);
	}
	else if (c/a == b){
		printf("%d+%d=%d\n", c, a, b);
	}
	
	//if answer is a
	if (c+b == c){
		printf("%d+%d=%d\n", c, b, a);
	}
	else if (c-b == a){
		printf("%d-%d=%d\n", c, b, a);
	}
	else if (b-c == a){
		printf("%d+%d=%d\n", b, c, a);
	}
	else if (c*b == a){
		printf("%d*%d=%d\n", c, b, a);
	}
	else if (c/b == a){
		printf("%d/%d=%d\n", c, b, a);
	}
	else if (b/c == a){
		printf("%d+%d=%d\n", b, c, a);
	}
			
}
