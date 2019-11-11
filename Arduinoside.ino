#define tempin A1
int temp = 0;

void setup() {
  // put your setup code here, to run once:
pinMode(tempin, INPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
temp = analogRead(tempin) ;//* 0.125 - 22.0;
Serial.println(temp);
delay(1000);
}