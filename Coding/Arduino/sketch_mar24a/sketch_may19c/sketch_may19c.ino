void setup() {
Serial.begin(9600);
}

void loop() {
 int a;
  if (Serial.available()) {
    a = Serial.read();
    if(a=='1'){
      analogWrite(9,255);
      Serial.println("Red on");
    }
    if(a=='0'){
      analogWrite(9,0);
      Serial.println("Red off");
    }
}
}
