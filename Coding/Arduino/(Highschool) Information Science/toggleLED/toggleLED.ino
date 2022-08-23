int btn1=3;
int led1=13;
int val1;
boolean toggleVal=false;

void setup() {
  Serial.begin(9600);
  pinMode(btn1,INPUT);
  pinMode(led1,OUTPUT);
}

void loop() {
  val1=digitalRead(btn1)
  if(val1==1){
    Serial.println(val1);
    toggleVal=!toggleVal;
  }
  if(toggleVal){
    digitalWrite(led1,HIGH);
  }
  else{
    digitalWrite(led1,LOW);
  }
  delay(200);

}
