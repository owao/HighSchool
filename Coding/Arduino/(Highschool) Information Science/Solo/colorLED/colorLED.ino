int Red=11;
int Blue=10;
int Green=9;
int val1;

void setup() {
  pinMode(Red,OUTPUT);
  pinMode(Blue,OUTPUT);
  pinMode(Green,OUTPUT);

}

void loop() {
  while (true){
    val1=analogRead(A0);
    analogWrite(Red,256-val1);
    analogWrite(Blue,val1);
    analogWrite(Green,128+val1);
    delay(10);
  }

}
