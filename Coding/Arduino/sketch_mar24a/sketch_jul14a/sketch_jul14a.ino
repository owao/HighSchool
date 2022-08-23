int a[7]={2,3,4,5,6,7,8};
int num[10][7]={
  {0,0,0,0,0,0,1},
  {1,0,0,1,1,1,1},
  {0,0,1,0,0,1,0},
  {0,0,0,0,1,1,0},
  {1,0,0,1,1,0,0},
  {0,1,0,0,1,0,0},
  {0,1,0,0,0,0,0},
  {0,0,0,1,1,1,1},
  {0,0,0,0,0,0,0},
  {0,0,0,0,1,0,0}
  };
void setup() {
  for(int i=0; i<7; i++){
  pinMode(i,OUTPUT);
  }
  pinMode(11, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(11)==LOW){
    int b=random(0,10);
    for(int i=0; i<7; i++){
   digitalWrite(a[i],num[b][i]);
    }
  }
  delay(100);
}
