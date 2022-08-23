int btn1=3;
int val1;

void setup() {
  Serial.begin(9600);
  pinMode(btn1,INPUT);
}

void loop() {
  val1=digitalRead(btn1);
  Serial.println(val1);

}
