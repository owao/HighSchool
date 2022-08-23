int TRIG=4;
int ECHO=3;
int RGB_Red=11;
int RGB_Green=10;
int RGB_Blue=9;
int LED=13;
int R;
int Buzzer=8;


void setup() {
  pinMode(LED,OUTPUT);
  pinMode(Buzzer,OUTPUT);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  Serial.begin(9600);
}

void loop() {
  R = analogRead(A0);
  float distance = getDistance( );
  
  if ( distance < 10 ) {  //초음파센서 앞에 물체가 없을 경우 가변저항에 따라 부품이 켜진다
    if (R<85){
      digitalWrite(LED,HIGH);
      digitalWrite(Buzzer,LOW);
      digitalWrite(RGB_Red, LOW);
      digitalWrite(RGB_Green, LOW);
      digitalWrite(RGB_Blue, LOW);
    }
    else if(R>170){
      digitalWrite(LED,LOW);
      digitalWrite(Buzzer,HIGH);
      digitalWrite(RGB_Red, LOW);
      digitalWrite(RGB_Green, LOW);
      digitalWrite(RGB_Blue, LOW);
    }
    else{
      digitalWrite(LED,LOW);
      digitalWrite(Buzzer,LOW);
      digitalWrite(RGB_Red, LOW);
      digitalWrite(RGB_Green, LOW);
      digitalWrite(RGB_Blue, HIGH);
    }
  }
  else { //초음파센서 앞에 물체가 있을 경우 작동이 꺼진다
    digitalWrite(LED,LOW);
    digitalWrite(Buzzer,LOW);
    digitalWrite(RGB_Red, LOW);
    digitalWrite(RGB_Green, LOW);
    digitalWrite(RGB_Blue, LOW);
  }

}

float getDistance( ) {
  digitalWrite(TRIG, LOW); // Trig LOW신호 입력
  delayMicroseconds(2); // 2μs 유지
  digitalWrite(TRIG,HIGH); // Trig HIGH신호 입력
  delayMicroseconds(10); // 10μs 유지
  digitalWrite(TRIG,LOW); // Trig LOW신호 입력
  long echoTime = pulseIn(ECHO, HIGH);
  float distance = (float)echoTime/29/2;
  Serial.print(distance);
  return distance;
}
