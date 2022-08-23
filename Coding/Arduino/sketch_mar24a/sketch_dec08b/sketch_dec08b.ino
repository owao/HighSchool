#include <Servo.h>
Servo myservo;
void setup() {      //조이스틱
  Serial.begin(9600); //digitalRead는 전기 신호를 판단해서 0과 1만 출력하기 때문에 여기서는 analogRead를 써야 함, 출력받는 값은 전압
  myservo.attach(9);
}

void loop() {
  int mapx=map(analogRead(A0), 0,683,1,179);  //입력핀, 변경전최소, 변경전최대, 변경후최소, 변경후최대
  myservo.write(mapx);
}
