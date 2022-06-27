#include <wiringPi.h>

//using default wPi numbering scheme
#define LED1 24
#define LED2 25

int main(){
    //initialize wiringPi
    wiringPiSetup();
    
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);

    while(1){
        digitalWrite(LED1, HIGH);
        delay(500);
        digitalWrite(LED1, LOW);

        digitalWrite(LED2, HIGH);
        delay(500);
        digitalWrite(LED2, LOW);
    }
    return 0;
}