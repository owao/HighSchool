#include <LedControl.h>
LedControl lc = LedControl(12,11,10,1);

void setup( ) {
  lc.shutdown(0,false); // 절전모드해제
  lc.setIntensity(0, 1); // 밝기 1 설정
  lc.clearDisplay(0); // 화면 지우기
}

void loop( ) {
  for(int i=0; i <= 7; i++) {
    if (i%2==0){
      lc.setRow(0,i,B10101010);
    }
    else{
      lc.setRow(0,i,B01010101);
    }
    delay(500);
  }
  for(int i=0; i <= 7; i++) {
    lc.setColumn(0,i,B00000000);
    delay(500);
  }
}
