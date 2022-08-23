int ledPin = 13;
int inputPin = 3;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(inputPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = digitalRead(inputPin);
  Serial.println(sensorValue);

  if (sensorValue){
    digitalWrite(ledPin, HIGH);
    Serial.println("LED ON");
  }
  else{
    digitalWrite(ledPin, LOW);
    Serial.println("LED OFF");
  }

  delay(200);
}
