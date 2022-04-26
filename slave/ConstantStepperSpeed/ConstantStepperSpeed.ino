//plainly spining stepper at constant speed and step
int pin1 = 9;
int pin2 = 10;
int pin3 = 11;
int pin4 = 12;
int state = 1;
int wait = 3;

void setup(){
Serial.begin(9600);

  pinMode(pin1,OUTPUT);
  pinMode(pin2,OUTPUT);
  pinMode(pin3,OUTPUT);
  pinMode(pin4,OUTPUT);
}

void loop(){
  switch(state){
    case 1:
    digitalWrite(pin1,HIGH);
    digitalWrite(pin2,LOW);
    digitalWrite(pin3,LOW);
    digitalWrite(pin4,LOW);
    delay(wait);
    state += 1;
    break;
    case 2:
    digitalWrite(pin1,LOW);
    digitalWrite(pin2,HIGH);
    digitalWrite(pin3,LOW);
    digitalWrite(pin4,LOW);
    delay(wait);
    state+=1;
    break;
    case 3:
    digitalWrite(pin1,LOW);
    digitalWrite(pin2,LOW);
    digitalWrite(pin3,HIGH);
    digitalWrite(pin4,LOW);
    delay(wait);
    state+=1;
    break;
    case 4:
    digitalWrite(pin1,LOW);
    digitalWrite(pin2,LOW);
    digitalWrite(pin3,LOW);
    digitalWrite(pin4,HIGH);
    delay(wait);
    state = 1;
    break;
  }
}
