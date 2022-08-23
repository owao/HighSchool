#include "pitches.h"
int melody[]={E4,D4,C4,D4,E4,0,E4,0,E4,0,D4,0,D4,0,D4,0,E4,0,E4,0,E4,0};
int beats[]={600,200,400,400,200,200,200,200,400,400,200,200,200,200,400,400,200,200,200,200,400,400};
void setup() {
  pinMode(8,OUTPUT);
  for(int i=0; i<(sizeof(melody)/sizeof(melody[0])); i++){
    tone(8,melody[i],beats[i]);
    delay(beats[i]);
  }
}

void loop() {

}
