#define TRIG 4
#define ECHO 3

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(TRIG, LOW); //Trig LOW 신호 입력
  delayMicroseconds(2); //2마이크로세컨드 유지
  digitalWrite(TRIG, HIGH); //Trig HIGH 신호 입력
  delayMicroseconds(10); // 10마이크로세컨드 유지
  digitalWrite(TRIG, LOW); //Trig LOW 신호 입력
  long echoTime=pulseIn(ECHO, HIGH);
  float distance= (float)echoTime/29/2;
  Serial.println(distance);
  delay(300);
}
