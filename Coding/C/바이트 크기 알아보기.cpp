#include <stdio.h>

int main(void)
{
	char	ch;
	short	sh;
	int num;
	float fnum=3.14;
	double dnum=3.14;
	
	int a=3.14;
	int b=129;
	char c=b;
	
	ch=sh=num=10;
	
	printf("����: %d,%d,%d, �Ǽ�: %f\n", ch,sh,num,fnum);
	printf("ch=%d\n", sizeof(ch));
	printf("sh=%d\n", sizeof(sh));
	printf("num=%d\n", sizeof(num));
	printf("fnum=%d\n", sizeof(fnum));
	printf("dnum=%d\n", sizeof(dnum));
	
	printf("%d\n", a);
	printf("%d", c);
	
}
