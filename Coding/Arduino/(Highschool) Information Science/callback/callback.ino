#define LED1 13
#define LED2 12
#define BUTTON 3
volatile int delayTime=1000;

void setup() {
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  attachInterrupt(1, ledOn, CHANGE);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(LED1, HIGH);
  delay(1000);
  digitalWrite(LED1, LOW);
  delay(1000);
}

void ledOn(){
  if(digitalRead(BUTTON)){
    digitalWrite(LED2, HIGH);
    Serial.print("LED ON");
  }
  else digitalWrite(LED2, LOW);
}
