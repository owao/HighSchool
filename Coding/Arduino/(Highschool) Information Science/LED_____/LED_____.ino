/***LED 13번 깜빡이기***/

//초기화
void setup() {
  pinMode(13,OUTPUT);
}
//main
void loop() {
  digitalWrite(13,HIGH);
  delay(1000);
  digitalWrite(13,LOW);
  delay(1000);
}
