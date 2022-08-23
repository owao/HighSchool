/* 작성일:5/19
 * 아날로그출력
 */

void setup() {
pinMode(9, OUTPUT);
pinMode(10, OUTPUT);
pinMode(11, OUTPUT);
}

void loop() {
for(int r=0;r<256;r++){
  analogWrite(9,r);
  analogWrite(10,255-r);
  analogWrite(11,0);
  delay(50);
}
/*digitalWrite(9,HIGH);
digitalWrite(10,HIGH);
digitalWrite(11,HIGH);
*/
}
