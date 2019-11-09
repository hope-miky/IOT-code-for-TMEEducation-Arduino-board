#define tempin A1
int temp = 0;

void setup() {
pinMode(tempin, INPUT);
Serial.begin(9600);
}

void loop() {
temp = analogRead(tempin) ;//* 0.125 - 22.0;
Serial.println(temp);
}