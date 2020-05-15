void setup() {
  //Sets baud rate for serial uart transmission
  Serial.begin(9600);
  while(!Serial){
  }
}

void loop() {
  //Reads from analog input pins 0 and 1 and sends
  //the data to the Raspberry Pi via Uart
  int val1, val2;
  val1 = analogRead(0);
  val2 = analogRead(1);
  Serial.println(val1);
  Serial.println(val2);
  delay(1000);
}
