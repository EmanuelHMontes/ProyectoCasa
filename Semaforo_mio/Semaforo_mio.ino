int LED_GREEN = 2;
int LED_YELLOW = 5;
int LED_RED = 18;
int LED_GREEN2 = 19;
int LED_YELLOW2 = 21;
int LED_RED2 = 23;
int pulsador = 21;




void setup() {
pinMode(pulsador,INPUT);
pinMode(LED_RED,OUTPUT);
pinMode(LED_GREEN,OUTPUT);
pinMode(LED_YELLOW,OUTPUT);
pinMode(LED_RED2,OUTPUT);
pinMode(LED_GREEN2,OUTPUT);
pinMode(LED_YELLOW2,OUTPUT);

}

void loop() 
{
 
digitalWrite(LED_RED,HIGH);
digitalWrite(LED_GREEN2,HIGH);
if(digitalRead(LED_RED)==HIGH)
  (digitalRead(LED_GREEN2)==HIGH);{
  digitalWrite(LED_YELLOW,LOW);
  digitalWrite(LED_YELLOW2,LOW);
  digitalWrite(LED_GREEN,LOW);
  digitalWrite(LED_RED2,LOW);
  delay(6000);
  digitalWrite(LED_RED,LOW);
  digitalWrite(LED_GREEN2,LOW);
  }
 digitalWrite(LED_GREEN,HIGH);
 digitalWrite(LED_RED2,HIGH);
 if(digitalRead(LED_RED)==LOW)
   (digitalRead(LED_GREEN2)==LOW);{
  digitalWrite(LED_RED,LOW);
  digitalWrite(LED_GREEN2,LOW);
  digitalWrite(LED_YELLOW,LOW);
  digitalWrite(LED_YELLOW2,LOW);
  delay(5000);
  digitalWrite(LED_GREEN,LOW);
  digitalWrite(LED_RED2,LOW);
  }
 digitalWrite(LED_YELLOW,HIGH);
 digitalWrite(LED_YELLOW2,HIGH);
 if(digitalRead(LED_GREEN)==LOW)
   (digitalRead(LED_RED2)==LOW);{
  digitalWrite(LED_GREEN,LOW);
  digitalWrite(LED_RED2,LOW);
  digitalWrite(LED_RED,LOW);
  digitalWrite(LED_GREEN2,LOW);
  for(int j=0;j<=3;j++)
{
  delay(1000);
  digitalWrite(LED_YELLOW,LOW);
  digitalWrite(LED_YELLOW2,LOW);
  delay(1000);
  digitalWrite(LED_YELLOW,HIGH); 
  digitalWrite(LED_YELLOW2,HIGH);
  }
digitalWrite(LED_YELLOW,LOW);
digitalWrite(LED_YELLOW2,LOW); 
  }
 }
