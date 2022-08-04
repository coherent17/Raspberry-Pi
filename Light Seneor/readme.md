# Light Sensor:

The resistance of the photo-resistor decreases when the intensity of the light increases.

## Circuit scheme
![](https://i.imgur.com/FiwpXsd.png)

Connect GND to GND, VCC to 5V, SIG to A0, and using digitalpin 7 as the output to the voltage of the LED.
![](https://i.imgur.com/Z4FXoqw.jpg)


## Arduino Code

```c=
const int pinLight = A0;
const int pinLED = 7;

int thresholdvalue = 50;

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
```

## Demo
{%youtube WSBgo-7lerI%}