#include <SoftwareSerial.h>
#include <AFMotor.h>
#define TRIG A2                     // 장애물 감지용 초음파센서
#define ECHO A3
AF_DCMotor motor_L(1);              // 모터드라이버 L293D  1: M1에 연결,  4: M4에 연결
AF_DCMotor motor_R(4); 

void setup() {
  Serial.begin(9600);              // PC와의 시리얼 통신속도
  Serial.println("Eduino Smart Car Start!");

  // turn on motor
  motor_L.setSpeed(230);              // 왼쪽 모터의 속도   
  motor_L.run(RELEASE);
  motor_R.setSpeed(230);              // 오른쪽 모터의 속도   
  motor_R.run(RELEASE);
  
  pinMode(TRIG,OUTPUT);               // 초음파 센서 세팅
  pinMode(ECHO,INPUT);

}

void loop() {
    int val1 = digitalRead(A0);    // 라인센서1 --> 적외선 센서로 교체
    int val2 = digitalRead(A5);    // 라인센서2 --> 적외선 센서로 교체

    float pre_time;
    float cur_time;

    digitalWrite(TRIG, HIGH);
    delay(10);
    digitalWrite(TRIG, LOW);
    float duration = pulseIn(ECHO, HIGH);                         //마이크로초
    float distance = ((float)(340*duration)/10000)/2;             //거리를 cm으로 변환

    pre_time = millis();
    
    if(pre_time - cur_time > 500 && distance <=5){                //0.5초마다 거리 감지 + 5cm 이내에 장애물이 있으면 정지
       motor_L.run(RELEASE); 
       motor_R.run(RELEASE);
    }
    else{    
        if (val1 == 0 && val2 == 0) {                   // 직진
          motor_L.run(FORWARD); 
          motor_R.run(FORWARD);
        }
        else if (val1 == 0 && val2 == 1) {              // 우회전
          motor_L.run(FORWARD); 
          motor_R.run(RELEASE);
        }
        else if (val1 == 1 && val2 == 0) {              // 좌회전
          motor_L.run(RELEASE); 
          motor_R.run(FORWARD);
        } 
        else if (val1 == 1 && val2 == 1) {              // 정지
          motor_L.run(RELEASE); 
          motor_R.run(RELEASE);
        }
    }
    Serial.print(distance);
    Serial.print("cm\n");                               //거리 출력(단위: cm)
    cur_time = millis();
}
    
