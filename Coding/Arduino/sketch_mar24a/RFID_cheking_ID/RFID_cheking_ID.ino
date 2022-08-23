#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN   9     // reset핀 설정
#define SS_PIN    10    // 데이터를 주고받는 역할의 핀( SS = Slave Selector )

MFRC522 mfrc(SS_PIN, RST_PIN);           // 이 코드에서 MFR522를 이용하기 위해 mfrc객체를 생성해 줍니다.

int LED_R = 3;                            // LED를 3번핀에 연결합니다.

void setup() {
  Serial.begin(9600);                     // 시리얼 통신, 속도는 9600
  SPI.begin();                             // SPI 초기화(SPI : 하나의 마스터와 다수의 SLAVE(종속적인 역활)간의 통신 방식)
  pinMode(LED_R, OUTPUT);                 // 3번핀을 출력으로 설정
  mfrc.PCD_Init();
}

void loop() {
  if ( ! mfrc.PICC_IsNewCardPresent() || ! mfrc.PICC_ReadCardSerial() ) {    //  태그 접촉이 되지 않았을때 또는 아이디가 읽혀지지 않았을때
    delay(200);        
    return;                                   // 0.2초 간격으로 값을 읽음
  }
    
  if(mfrc.uid.uidByte[0] == 196 && mfrc.uid.uidByte[1] == 200 
       && mfrc.uid.uidByte[2] == 97 && mfrc.uid.uidByte[3] == 30) {    // 2번 태그 ID가 맞을경우
    digitalWrite(LED_R, HIGH);                // 3번핀 에 연결된 led 켜지기 
    Serial.println("Hello, Eduino~");        // 시리얼 모니터에 "Hello, Eduino~" 출력
    delay(1000);
    digitalWrite(LED_R, LOW);
  }
  else {                                   // 다른 태그 ID일 경우
    for(int i=0;i<5;i++){
      digitalWrite(LED_R, HIGH);
      delay(200);
      digitalWrite(LED_R, LOW);
      delay(200);
    }
    Serial.println("Who are you?");        // 시리얼 모니터에 "Who are you?" 출력 
  }  
}
//[출처] [아두이노 강좌] RFID를 이용한 태그별 LED 및 Buzzer 제어|작성자 에듀이노 오픈랩

//채터링 방지(카드를 대고 있을 때 계속 값을 읽어들이지 못하도록, 한 번만 값을 받도록 하는 방법)를 해 보는 것도 좋은 개선안임
