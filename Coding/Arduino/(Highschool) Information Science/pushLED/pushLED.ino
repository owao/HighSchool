int btn1=3;
int led1=13;
int val1;

void setup() {
  pinMode(btn1,INPUT)
  pinMode(led1,OUTPUT);
}

void loop() {
  val1=digitalRead(btn1);
  digitalWrite(led1,val1);

}
