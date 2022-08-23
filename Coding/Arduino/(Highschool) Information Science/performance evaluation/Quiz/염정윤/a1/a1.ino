int val;

void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop() {
  if (Serial.available() > 1){
    val=Serial.read();
    if (val>=1 && val<10){
      analogWrite(13,HIGH);
      Serial.println("LED ON");
    }
    else if (val>=10 && val<20){
      analogWrite(13,LOW);
      Serial.println("LED OFF");
    }
    else{
      Serial.println("정확한 범위 안에서 숫자를 입력하세요");
    }
  }

}
