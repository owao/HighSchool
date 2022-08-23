

void setup() {
  for(int i=2; i<=9; i++){
    pinMode(i,OUTPUT);
  }
}

void loop() {
  digitalWrite(2,LOW); //X
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
  digitalWrite(5,LOW); //X
  digitalWrite(6,LOW); //X
  digitalWrite(7,LOW);
  digitalWrite(8,LOW);
  digitalWrite(9,LOW); //X
}
