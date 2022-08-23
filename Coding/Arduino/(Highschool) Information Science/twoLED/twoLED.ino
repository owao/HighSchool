#define LED1 13
#define LED2 12
#define BUTTON 11
unsigned long currentTime=0;
unsigned long previousTime=0;
boolean onOff = false;

void setup() {
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(BUTTON, INPUT);

}

void loop() {
  currentTime=millis();
  if(currentTime>previousTime+1000){
    if(onOff) digitalWrite(LED1, HIGH);
    else digitalWrite(LED1,LOW);
    onOff =! onOff;
    previousTime=currentTime;
  }
  if(digitalRead(BUTTON)) digitalWrite(LED2, HIGH);
  else digitalWrite(LED2, LOW);

}
