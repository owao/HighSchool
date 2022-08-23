#include <Servo.h>
Servo myservo;
int a=0;

void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(2)==0 and a==0){
    while(digitalRead(2)==0);
    delay(20);
    myservo.write(20);
    delay(500);
    a=1;
  }
  else if (digitalRead(2)==0 and a==1){
    while(digitalRead(2)==0);
    delay(20);
    myservo.write(150);
    delay(500);
    a=0;
  }
}
