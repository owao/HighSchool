#include <SoftwareSerial.h>
SoftwareSerial BTserial(12, 13);
char data;
void setup() {
  BTserial.begin(9600);
}

void loop() {
  if (BTserial.available()){
    data=BTserial.read();
    if (data=='1'){
      digitalWrite(13, HIGH);
    }
    else if (data=='0'){
      digitalWrite(13, LOW);
    }
  }

}
