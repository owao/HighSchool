int a=0;
void setup() {
  pinMode(5, INPUT);
  pinMode(6, INPUT_PULLUP);
  Serial.begin(9600);
  pinMode(7, OUTPUT);
}

void loop() {
Serial.println(digitalRead(5));
if(digitalRead(5)==0 and a==0){
  while(digitalRead(5)==0);
  digitalWrite(7,1);
  a=1;
}
else if(digitalRead(5)==0 and a==1){
  while(digitalRead(5)==0);
  digitalWrite(7,0);
  a=0;
}
}
