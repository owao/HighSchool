void setup() {
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  Serial.begin(9600);
}

  void loop() {
  Serial.print("hi");
  if(Serial.available())
}
