#include <Stepper.h>
Stepper step1(2048, 11, 9, 10, 8);
int lap = 2048;

void setup() {
  step1.setSpeed(15);
}

void loop() {
  step1.step(lap);
  delay(500);
  step1.step(-lap);
  delay(500);
}
