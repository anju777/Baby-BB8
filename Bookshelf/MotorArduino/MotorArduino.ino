int speedPin1 = 3; // H-bridge enable pin for speed control
int motor1APin = 6; // H-bridge leg 1
int motor2APin = 7; // H-bridge leg 2

int speedPin2 = 5;
int motor3APin = 2;
int motor4APin = 8;

int speed_value_motor1; // value for motor speed
int speed_value_motor2;

int command;

void setup() {
 // set digital i/o pins as outputs:
 pinMode(speedPin1, OUTPUT);
 pinMode(motor1APin, OUTPUT);
 pinMode(motor2APin, OUTPUT);

 pinMode(speedPin2, OUTPUT);
 pinMode(motor3APin, OUTPUT);
 pinMode(motor4APin, OUTPUT);
 
 Serial.begin(9600);

}

// Winkler, DC motor control with the Arduino board, p.2
void loop() {

 // control the speed 0- 255
 speed_value_motor1 = 255; // full speed
 speed_value_motor2 = 255;
 
 analogWrite(speedPin1, speed_value_motor1); // output speed as PWM value
 analogWrite(speedPin2, speed_value_motor2);
 
 if (Serial.available() > 0) {
   command = Serial.parseInt();
   if (command > 5 || command < 1) {
     Serial.println("what ??"); 
   }
   else {
     switch (command) {
       case 1:
         Serial.println("forward");
         break;
       case 2:
         Serial.println("backward");
         break;
       case 3:
         Serial.println("left");
         break;
       case 4:
         Serial.println("right");
         break;
       case 5:
         Serial.println("brake");
         break;  
     }
   }
 }
   
   
 switch (command) {
     case 1: //forward
       digitalWrite(motor1APin, LOW); 
       digitalWrite(motor2APin, HIGH);
       
       digitalWrite(motor3APin, LOW);
       digitalWrite(motor4APin, HIGH);
       break;
     case 2: //backward
       digitalWrite(motor1APin, HIGH);
       digitalWrite(motor2APin, LOW);
       
       digitalWrite(motor3APin, HIGH);
       digitalWrite(motor4APin, LOW);
       break;
     case 3: //left
       digitalWrite(motor1APin, LOW);
       digitalWrite(motor2APin, LOW);
       
       digitalWrite(motor3APin, LOW);
       digitalWrite(motor4APin, HIGH);
       break;
     case 4: //right
       digitalWrite(motor1APin, LOW); 
       digitalWrite(motor2APin, HIGH);
       
       digitalWrite(motor3APin, LOW);
       digitalWrite(motor4APin, LOW);
       break;
     case 5: //brake
       digitalWrite(motor1APin, LOW); 
       digitalWrite(motor2APin, LOW);
       
       digitalWrite(motor3APin, LOW);
       digitalWrite(motor4APin, LOW);
       break;
   }
}
