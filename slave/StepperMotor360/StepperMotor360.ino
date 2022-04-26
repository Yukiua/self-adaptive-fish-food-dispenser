#include <Stepper.h>

const int stepsPerRevolution = 1024;  // change this to fit the number of steps per revolution
int speeds;
unsigned long new_time;
unsigned long old_time;
int directions;
float chara = 0.8;
// initialize the stepper library on pins 8 through 11:
// blue -> 9,pink ->10,yellow->11,orange->12
Stepper myStepper(stepsPerRevolution, 9, 11, 10, 12);

void setup() {
  myStepper.setSpeed(1);
}

void loop() {
  new_time = millis();
  String chars = Serial.readStringUntil('\n');
  if(chars != 0){chara = chars.toFloat();}
  speeds      = floor(chara * 18);
  if(speeds>0) { directions = 1; }
  else { directions = -1; }
  myStepper.setSpeed(abs(speeds));
  myStepper.step(stepsPerRevolution * directions);
  Serial.print(new_time - old_time);
  Serial.print(",");
  Serial.print(speeds);
   old_time = new_time;
}
