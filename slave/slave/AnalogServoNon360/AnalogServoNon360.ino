#include "Servo.h"

Servo myservo;
int speeds = 50;
int pos = 0;

void setup() {
  myservo.attach(9);
  Serial.begin(9600);
}

void loop() {
  Serial.println(speeds);
  String chara = Serial.readStringUntil('\n');
  if (chara.equals("fast"))
  {
    speeds = 10;
  }
  else if (chara.equals("mid"))
  {
    speeds = 25;
  }
  else if (chara.equals("slow"))
  {
    speeds = 50;
  }
  for (pos = 0; pos <= 180; pos += 5) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(speeds);                       // waits 15 ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 5) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(speeds);                       // waits 15 ms for the servo to reach the position
  }
}
