int clapCount=0;
int val;

void setup() {
  Serial.begin(9600);
}

void loop() {
  val=analogRead(A0);
  if(val>560){
    Serial.println(++clapCount);
    delay(100);
  }

}
