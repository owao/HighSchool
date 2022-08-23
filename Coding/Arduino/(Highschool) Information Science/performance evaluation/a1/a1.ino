#include <SoftwareSerial.h> // 블루투스 라이브러리 선언
#include <LedControl.h> //LED모듈 선언
LedControl lc = LedControl(12,11,10,1);

void setup() {
  pinMode(8,INPUT); //적외선센서
  SoftwareSerial bt (2,3); //블루투스 객채 생성-TX:2 RX:3
  Serial.begin(9600); //시리얼 통신 시작
  bt.begin(9600); //블루투스 통신 시작
  lc.shutdown(0,false); // 절전모드해제
  lc.setIntensity(0, 1); // 밝기설정
  lc.clearDisplay(0); // 화면 지우기
}

void loop() {
  if (bt.available()>0){ //블루투스 신호가 존재한다면
    mode=bt.read(); //시스템 온오프 모드
    if (mode=='SYSTEM OFF’){ //시스템 오프
      lc.clearDisplay(0); //매트릭스 끄기
    }      
    else if (mode=='SYSTEM ON’){ //시스템 온
      if (digitalRead(8)==LOW){
        lc.setRow(0,0,B10000001);
        lc.setRow(0,1,B01000010);
        lc.setRow(0,2,B00100100);
        lc.setRow(0,3,B00011000);
        lc.setRow(0,4,B00011000);
        lc.setRow(0,5,B00100100);
        lc.setRow(0,6,B01000010);
        lc.setRow(0,7,B10000001);
        if (bt.available()>0){ //블루투스 신호가 존재한다면
          closing=bt.read(); //X표시를 끌 신호
          if (closing=='확인'){ //정상적인 신호가 왔다면
            lc.clearDisplay(0); //매트릭스 끄기
          }
        }
      }
    }
      
  }
}
