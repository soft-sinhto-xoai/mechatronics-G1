// 4 servo motors system
// Potentiometers are used for input

#include <Servo.h>

Servo servo_12; // define variable
Servo servo_11;
Servo servo_10;
Servo servo_9;

void setup() 
{
  servo_12.attach(12); // assign pin for servo signal
  servo_11.attach(11);
  servo_10.attach(10);
  servo_9.attach(9);
  pinMode(A0, INPUT); // set a0~3 as input
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(8, INPUT);
  Serial.begin(9600);
}

void loop()
{
  float s0 = analogRead(A0); // read potentiometer signal
  float s1 = analogRead(A1);
  float s2 = analogRead(A2);
// convert signal of potentiometer to angle
  float ang0 = s0/1023*180;
  float ang1 = s1/1023*180;
  float ang2 = s2/1023*180;
  
  float fb_ang0 = servo_10.read();
  if (abs(fb_ang0-ang0)>1)
  {
    servo_10.write(ang0);
    delay(20);
  }

  float fb_ang1 = servo_11.read();
  if (abs(fb_ang1-ang1)>0.5)
  {
    servo_11.write(ang1);
    delay(20);
  }
  
  float fb_ang2 = servo_12.read();
  if (abs(fb_ang2-ang2)>0.5)
  {
    servo_12.write(ang2);
    delay(20);
  }
  
  if (digitalRead(8) == HIGH) {
    servo_9.write(90); // when the switch on, rotate
  } else {
    servo_9.write(0); // when off, original state
  }
  // check ang variables
  Serial.print("Motor 0:"); Serial.print("\n");
  Serial.print("Control ang:"); Serial.print(ang0); Serial.print(", ");
  Serial.print("Feedback ang:");Serial.print(fb_ang0); Serial.print("\n");
  
  Serial.print("Motor 1:"); Serial.print("\n");
  Serial.print("Control ang:"); Serial.print(ang1); Serial.print(", ");
  Serial.print("Feedback ang:");Serial.print(fb_ang1); Serial.print("\n");
  
  Serial.print("Motor 2:"); Serial.print("\n");
  Serial.print("Control ang:"); Serial.print(ang2); Serial.print(", ");
  Serial.print("Feedback ang:"); Serial.print(fb_ang2); Serial.print("\n");

  Serial.println(digitalRead(8));
  delay(1000); // wait 100 milliseconds
}
