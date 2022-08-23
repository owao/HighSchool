void setup() {
  pinMode(3,INPUT); //버튼
  pinMode(9,OUTPUT); //부저
}

void loop() {
  int a=analogRead(3);

  if (a==1){
    digitalWrite(9,HIGH);
  }
}
