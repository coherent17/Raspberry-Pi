#include <wiringPi.h>
#include <signal.h>

//using default wPi numbering scheme
#define LED1 18

int blink = 1;

void cleanup(int signal){
    blink = 0;
    digitalWrite(LED1, LOW);
    pinMode(LED1, INPUT);
}

int main(){

    //setting the abrupt condition
    signal(SIGINT, cleanup);    //if user press ctrl + c, then do cleanup
    signal(SIGTERM, cleanup);   //if program terminated with kill command
    signal(SIGHUP, cleanup);    //if terminal windows closed

    //initialize wiringPi
    wiringPiSetupGpio();    // <- change to Gpio
    pinMode(LED1, PWM_OUTPUT);

    while(blink){
        //become brighter
        for(int i = 0; i < 1024; i++){
            pwmWrite(LED1, i);
            delay(1);
        }

        //become darker
        for(int i = 1023; i >= 0; i--){
            pwmWrite(LED1, i);
            delay(1);
        }
    }
    return 0;
}