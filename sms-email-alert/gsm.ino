#include <SoftwareSerial.h>

//Create software serial object to communicate with SIM800L
SoftwareSerial mySerial(11,10); //SIM800L Tx & Rx is connected to Arduino #3 & #2;

void setup(){
  mySerial.begin(9600);   // Setting the baud rate of GSM Module  
  Serial.begin(9600);    // Setting the baud rate of Serial Monitor (Arduino)
  delay(100);
  
  
  randomSeed(analogRead(0)); // nothing connected to 0 so read sees noise
  int i;
  float c;
  int house1=500;
  Serial.println("HOUSE 1:");
  Serial.print("Total electricity provided : ");
  Serial.print(house1);
  Serial.println("units");
  Serial.println("Electricity consumed in 5 days:");
  float b=0;
  float d=0;
  for (i=0;i<5;i++)
  {
  float randNumber = random(50,150); // generate random number between 50 & 150
  
  float a=randNumber;
  
  Serial.println(a); // show the value in Serial Monitor
  if (a>b){
    c=a-b;
    b=a;
    mySerial.println("AT+CMGF=1");    //Sets the GSM Module in Text Mode
    delay(2000);  // Delay of 2000 milli seconds or 2 second
    mySerial.println("AT+CMGS=\"+918360276731\"\r"); // Replace x with mobile number
    delay(2000);
    mySerial.print("Power consumed is :");// The SMS text you want to send
    delay(2000);
    mySerial.println(a);
    delay(2000);
    mySerial.print("Power consumed is");
    delay(2000);
    mySerial.print(c);
    delay(2000);
    mySerial.println(" more than previous value");
  
    delay(2000);
    mySerial.println((char)26);// ASCII code of CTRL+Z
    delay(2000);
  }
  else if(a<b){
    c=b-a;
    b=a;
    mySerial.println("AT+CMGF=1");    //Sets the GSM Module in Text Mode
    delay(2000);  // Delay of 1000 milli seconds or 1 second
    mySerial.println("AT+CMGS=\"+918360276731\"\r"); // Replace x with mobile number
    delay(2000);
    mySerial.print("Power consumed is :");// The SMS text you want to send
    delay(2000);
    mySerial.println(a);
    delay(2000);
    mySerial.print("Power consumed is");
    delay(2000);
    mySerial.print(c);
    delay(2000);
    mySerial.println(" less than previous value");
  
    delay(2000);
    mySerial.println((char)26);// ASCII code of CTRL+Z
    delay(2000);
  }
  d+=a;
  if (d>250){
    mySerial.println("You have exhausted 50% of your energy.");
  }
  if (d>450){
    mySerial.println("You have exhausted 90% of your energy.");
  }
    
  
  
}
}



void loop(){
  
}
