int RGB_Red=11;
int RGB_Green=10;
int RGB_Blue=9;
int LED=13;
int R;
int Button=3;
int Buzzer=8;

int Sign;  //채널을 돌릴 변수
int B; //버튼 누른 값
boolean toggleVal = false; //버튼을 껐다켰다

unsigned long currentTime = 0;
unsigned long previousTime = 0;
boolean onOff = false;

void setup() {
  pinMode(LED,OUTPUT);
  pinMode(Button,INPUT);
  pinMode(Buzzer,OUTPUT);
}

void loop() {
  R = analogRead(A0);
  
  if ( R < 512 ){
    digitalWrite(RGB_Red, HIGH);
    digitalWrite(RGB_Green, LOW);
    digitalWrite(RGB_Blue, LOW);
    Sign=0;
  }
  else{
    digitalWrite(RGB_Red, LOW);
    digitalWrite(RGB_Green, LOW);
    digitalWrite(RGB_Blue, HIGH);
    Sign=1; 
  }
  
  B = digitalRead(Button);
  if ( B == 1 ){
    toggleVal =! toggleVal;
  }
  if ( toggleVal ){
    digitalWrite(LED,HIGH);
  }
  else{
    digitalWrite(LED,LOW);
  }
  delay(200);

}
