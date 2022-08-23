#define IRsensor 8
#define LED 13
void setup( ) {
  pinMode(IRsensor, INPUT);
  pinMode(LED, OUTPUT);
}
void loop( ) {
  if ( digitalRead( IRsensor ) == LOW ) digitalWrite(LED, HIGH);
  else digitalWrite(LED, LOW);
}
