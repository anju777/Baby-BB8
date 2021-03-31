int speedPin1 = 3; // H-bridge enable pin for speed control
int motor1APin = 6; // H-bridge leg 1
int motor2APin = 7; // H-bridge leg 2

int speedPin2 = 5;
int motor3APin = 2;
int motor4APin = 8;

int speed_value_motor1; // value for motor speed
int speed_value_motor2;

void setup() {
 // set digital i/o pins as outputs:
 pinMode(speedPin1, OUTPUT);
 pinMode(motor1APin, OUTPUT);
 pinMode(motor2APin, OUTPUT);

 pinMode(speedPin2, OUTPUT);
 pinMode(motor3APin, OUTPUT);
 pinMode(motor4APin, OUTPUT);

}

void loop() {

 // control the speed 0- 255
 speed_value_motor1 = 255; // full speed
 speed_value_motor2 = 255;
 
 analogWrite(speedPin1, speed_value_motor1); // output speed as PWM value
 analogWrite(speedPin2, speed_value_motor2);
 
 digitalWrite(motor1APin, LOW); 
 digitalWrite(motor2APin, HIGH);
 
 digitalWrite(motor3APin, LOW);
 digitalWrite(motor4APin, HIGH);
   
}
