#include <LiquidCrystal_I2C.h> //LCD 실행
LiquidCrystal_I2C lcd(0x27, 16,2); //LCD 객체 생성
int clapCount=0; //박수 개수
long timer=millis(); //시간 세기

void setup( ) {
  pinMode(8,INPUT); //사운드센서
  lcd.init(); // 초기화
  lcd.backlight(); // 백라이트 켜기
}

void loop() {
  timer=0; //시작할 때 시간 초기화
  if (digitalRead(8)==HIGH){ //박수 감지
    clapCount=++clapCount; //박수 개수가 늘어난다
    delay(100); // 0.1초 기다리기(연속감지 방지)
    if(digitalRead(8)==LOW){ //박수가 끊긴다면
      if(timer>3000){ //그리고 끊긴 지 3초 이상 지난다면
        lcd.setCursor(1,0); // 커서 이동
        lcd.print("count:"); //윗줄 입력
        lcd.setCursor(7,1); // 커서 이동
        lcd.print(clapCount); //아랫줄(숫자)입력
        clapCount=0; //박수 개수 초기화
      }
    }
  }
}
