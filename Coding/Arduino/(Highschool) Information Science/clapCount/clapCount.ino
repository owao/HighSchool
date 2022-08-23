#define soundSensor 8 //사운드 센서
int clapCount = 0; //박수 개수

void setup() {
  Serial.begin(9600);
  pinMode(soundSensor, INPUT);
}

void loop() {
  if(digitalRead(soundSensor)==HIGH) { //소리 감지
    Serial.println(++clapCount);
    delay(100);
  }

}
