#include <Servo.h>
#define RMS 5
#define RMP 6
#define RMN 7
#define LMS 4
#define LMP 2
#define LMN 3

const int trigPin = 12;
const int echoPin = 11;

float duration, distance;

void setup() {
  pinMode(8, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(RMS, OUTPUT);
  pinMode(RMP, OUTPUT);
  pinMode(RMN, OUTPUT);
  pinMode(LMS, OUTPUT);
  pinMode(LMP, OUTPUT);
  pinMode(LMN, OUTPUT);
  digitalWrite(RMS, HIGH);
  digitalWrite(LMS, HIGH);
  
  Serial.begin(9600);
}

void loop() {
  sense();
  
  if(distance>100)
  {
    forward();
  }
  else
  {
    stops();
    digitalWrite(8, HIGH);
    delay(1000);
    digitalWrite(8, LOW);
    delay(1000);
  } 
 
}

void sense()
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration*.0343)/2;
  Serial.print("Distance: ");
  Serial.println(distance);
  delay(100);
}

void forward()
{ 
  digitalWrite(RMP, HIGH);
  digitalWrite(RMN, LOW);
  digitalWrite(LMP, HIGH);
  digitalWrite(LMN, LOW);
 }



void stops()
{
  digitalWrite(RMP, LOW);
  digitalWrite(RMN, LOW);
  digitalWrite(LMP, LOW);
  digitalWrite(LMN, LOW);
}

