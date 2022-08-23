void setup() {
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  analogWrite(9,analogRead(A1)/4);
  analogWrite(10,analogRead(A2)/4);
  analogWrite(11,analogRead(A3)/4);
  Serial.println(analogRead(A1));
  Serial.println(analogRead(A2));
  Serial.println(analogRead(A3));
}
