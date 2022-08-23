//Einstein's Puzzle Solver
//created by Kim Yongmook ( http://moogi.new21.org )
//Originically created on December 1, 2000

#include <stdio.h>
#include <stdlib.h>
 
#ifdef __cplusplus
#define DECLARE_SYMBOL(category, num, el1, el2, el3, el4, el5) \
	const int category=num; \
	enum tag##category { el1,el2,el3,el4,el5 }; \
	const char *str##category[5]={ #el1, #el2, #el3, #el4, #el5 };
#else
#define DECLARE_SYMBOL(category, num, el1, el2, el3, el4, el5) \
	enum tag##category { el1,el2,el3,el4,el5 }; \
	const char *str##category[5]={ #el1, #el2, #el3, #el4, #el5 };
#define COUNTRY  0
#define COLOR	1
#define BEVERAGE 2
#define PET	  3
#define CIGARET  4
#endif

DECLARE_SYMBOL(COUNTRY,  0, England, German, Sweden, Norway, Denmark)
DECLARE_SYMBOL(COLOR,	1, red, green, blue, yellow, white)
DECLARE_SYMBOL(BEVERAGE, 2, red_tea, water, milk, coffee, beer)
DECLARE_SYMBOL(PET,	  3, dog, cat, horse, bird, goldfish)
DECLARE_SYMBOL(CIGARET,  4, bland, danhill, blue_master, pallmall, prince)

int permu[120][5];

void create_permutation(const int *used, int pos)
{
	static int cnt=0; static int making[5];
	int tmp[5]={0,},i;

	if(pos==5) {
		for(i=0;i<5;i++) permu[cnt][i]=making[i]; cnt++; return;
	}
 
	for(i=0;i<5;i++) tmp[i]=used[i];
	for(i=0;i<5;i++)
		if(!used[i]) {
			tmp[i]=1; making[pos]=i; create_permutation(tmp, pos+1); tmp[i]=0;
		}
}

typedef struct { int idx[5]; } HOUSE;
HOUSE hou[5];

const HOUSE *find_at(int category, int value)
{
	int i;
	for(i=0;i<5;i++) if(hou[i].idx[category]==value) return &hou[i];
	return NULL;
}

void calculate(const int *seq, int pos)
{
	int i;
	if(pos==5) return;

	//�� ���� �оߺ� ���� seq(���Ե� ���� ��)�� ������ �Ѵ�.
	for(i=0;i<5;i++) hou[i].idx[pos]=seq[i];

	switch(pos) {
	case COUNTRY:
		//9: �븣�������� ù ��° ���� ���.
		if(hou[0].idx[COUNTRY]!=Norway) return;
		break;
	case COLOR:
		//14: �븣�������� �Ķ��� �� ������ ���.
		if(hou[1].idx[COLOR]!=blue) return;

		//4: ������� ����� ���ʿ� �ִ�.
		if( ! ( (hou[2].idx[COLOR]==green && hou[3].idx[COLOR]==white) ||
			(hou[3].idx[COLOR]==green && hou[4].idx[COLOR]==white) ) ) return;

		//1: �������� ������ ���� ���.
		if(find_at(COUNTRY, England)->idx[COLOR]!=red) return;
		break;
	case BEVERAGE:
		//8: �Ѱ�� ����� ������ ���Ŵ�.
		if(hou[2].idx[BEVERAGE]!=milk) return;

		//3: ����ũ ����� ȫ���� ���Ŵ�.
		if(find_at(COUNTRY, Denmark)->idx[BEVERAGE]!=red_tea) return;

		//5: ����� ����� Ŀ�Ǹ� ���Ŵ�.
		if(find_at(COLOR, green)->idx[BEVERAGE]!=coffee) return;
		break;
	case PET:
		//2: ������ ����� ���� Ű���
		if(find_at(COUNTRY,Sweden)->idx[PET]!=dog) return;
		break;
	case CIGARET:
		//6: ���� ��踦 �ǿ�� ����� ���� Ű���
		if(find_at(CIGARET,pallmall)->idx[PET]!=bird) return;

		//7: ����� �� ����� ���� ��踦 �ǿ��
		if(find_at(COLOR,yellow)->idx[CIGARET]!=danhill) return;

		//10: ���� ��踦 �ǿ�� ����� ����� Ű��� ��� ������ ���
		if(abs( find_at(CIGARET,bland)-find_at(PET,cat) )!=1) return;

		//11: ���� Ű��� ����� ���� ��踦 �ǿ�� ��� ������ ���
		if(abs( find_at(CIGARET,danhill)-find_at(PET,horse) )!=1) return;

		//12: ��� �Ž��� ��� �Ǵ� ����� ���ָ� ���Ŵ�
		if(find_at(CIGARET,blue_master)->idx[BEVERAGE]!=beer) return;

		//13: �������� ������ ��踦 �ɴ�
		if(find_at(COUNTRY,German)->idx[CIGARET]!=prince) return;

		//15: ���� ��踦 �ǿ�� ����� �� ���ô� ��� ������ ���
		if(abs( find_at(CIGARET,bland)-find_at(BEVERAGE,water) )!=1) return;
		break;
	}

	if(pos==4) {
		printf("%s\n", strCOUNTRY[ find_at(PET,goldfish)->idx[COUNTRY] ]);
	}
	for(i=0;i<120;i++) calculate(permu[i],pos+1); //pos���� �� �ܰ� �Ʒ��ܰ�� ��������.
}

int main()
{
	int t[5]={0,}; int i;
	create_permutation(t,0);
	for(i=0;i<120;i++) calculate(permu[i],0);
	return 0;
}
