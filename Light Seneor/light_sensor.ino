const int pinLight = A0;
const int pinLED = 7;

int thresholdvalue = 200;

void setup() {
    pinMode(pinLED, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int sensorValue = analogRead(pinLight);
    if(sensorValue < thresholdvalue){
        digitalWrite(pinLED, HIGH);
    }
    else{
        digitalWrite(pinLED, LOW);
    }
    Serial.print("Sensor = ");
    Serial.println(sensorValue);
    delay(200);
}