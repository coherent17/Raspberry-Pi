#include <wiringPi.h>
#include <signal.h>

//using default wPi numbering scheme
#define LED1 24
#define LED2 25

int blink = 1;

void cleanup(int signal){
    blink = 0;
}

int main(){

    //setting the abrupt condition
    signal(SIGINT, cleanup);    //if user press ctrl + c, then do cleanup
    signal(SIGTERM, cleanup);   //if program terminated with kill command
    signal(SIGHUP, cleanup);    //if terminal windows closed

    //initialize wiringPi
    wiringPiSetup();
    
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);

    while(blink){
        digitalWrite(LED1, HIGH);
        delay(500);
        digitalWrite(LED1, LOW);

        digitalWrite(LED2, HIGH);
        delay(500);
        digitalWrite(LED2, LOW);
    }

    digitalWrite(LED1, LOW);
    digitalWrite(LED2, LOW);
    pinMode(LED1, INPUT);
    pinMode(LED2, INPUT);

    return 0;
}