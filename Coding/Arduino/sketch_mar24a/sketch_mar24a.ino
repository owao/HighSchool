/* 2018.3.24
 *  내용 : led 제어
 *  
 *  전원 = 5v = (+) = 1 = HIGH = 참
 *  접지 = 0V = (-) = 0 = LOW = 거짓
 *  
 *  2018.4.7.
 *  while() : 무한 반복, 횟수가 정해지지 않은 반복
 *  for() : 횟수가 정해진 반복
 *  
 *  while(조건) {
 *   실행 1
 *   }
 *   실행 2
 *  조건이 참이면 실행 1을 무한반복
 *  조건이 거짓이면 실행 2로 넘어감
 *  
 *  num (변수)
 *  int num; -> 0진수, 정수
 *  
 *  for(변수; 비교값; 증감연산자)
 *  ex) for(i=0; i<3; I+1;)
 *  
 *  i++    ==    i=i+1
 *  
 *  for (int i = 0; i < 256; i = i + 2) {
    analogWrite(3, i);
    delay(50);
  }
  불이 점점 켜지는 함수
 *  for (int i = 250; i > 0; i = i - 5) {
    analogWrite(3, i);
    delay(50);
  }
  불이 점점 꺼지는 함수
 */
void setup() {
 pinMode(3, OUTPUT);
 pinMode(5, OUTPUT);
}

void loop() {
    for (int i = 0; i < 250; i = i + 5) {
    analogWrite(5, i);
    delay(50);
  }
  for (int i = 250; i > 0; i = i - 5) {
    analogWrite(3, i);
    delay(50);
  }
  delay(200);
    for (int i = 250; i > 0; i = i - 5) {
    analogWrite(5, i);
    delay(50);
  }
    for (int i = 0; i < 250; i = i + 5) {
    analogWrite(3, i);
    delay(50);
  }
  delay(200);

  }
