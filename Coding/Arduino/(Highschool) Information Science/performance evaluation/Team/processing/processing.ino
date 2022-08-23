//조도센서 선 A0에 연결
//사운드센서도 같은 방식으로 동작 가능. 부품만 갈면 됨

int val;

void setup(){
  Serial.begin(9600); //시리얼 통신 시작
}

void loop(){
  val = map(analogRead(A0),600,1000,0,127);
  Serial.write(0xff); //아스키코드를 거치지 않고 16진수로 값을 내보냄
  Serial.write((val >> 8) & 0xff);
  Serial.write(val & 0xff);
  delay(70);
}
