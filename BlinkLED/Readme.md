# Blink LED with RaspberryPi
[TOC]
## Instaling WiringPi Package

type following command to install WiringPi
```bash = 
$ docker run --rm --device /dev/ttyAMA0:/dev/ttyAMA0 --device /dev/mem:/dev/mem --privileged -ti python:2 /bin/sh
$ apt-get update && apt-get install git-core sudo
$ git clone https://github.com/WiringPi/WiringPi --depth 1
$ cd WiringPi/
$ ./build
$ cd ..
```

## Circuit Diagram
![](https://i.imgur.com/z5EkbJc.png)
![](https://i.imgur.com/IXOkyDn.jpg)

Connect resistors to GPIO port 19 and 26 which follows BCM numbering scheme (wpi 24 25) and connect LED with correct polarity.

## BlinkLED With Bash Shell

### Monitor the state of all GPIO pins:
```bash=
$ gpio readall
```
The print out format is same as the layout on RaspberryPi.

![](https://i.imgur.com/oHRAOCw.png)
![](https://i.imgur.com/zLbhUXu.png)

### Blink the LED
When using command to control the pinMode must use wPi number system.
![](https://i.imgur.com/tVP9kMr.png)
For example, if we want to turn on the LED connect to GPIO 19 (wPi 24), we need to type following commands.
```bash=
$ gpio mode 24 out
$ gpio write 24 1
```

And the LED connect to GPIO 19 in on.
![](https://i.imgur.com/bVgkzC5.jpg)

And now using gpio readall command to monitor the pin state, we can see the Mode has turned to OUT and the state is HIGH(1).
![](https://i.imgur.com/kggpgJu.png)

And the voltage across the LED is almost 3.3(V).
![](https://i.imgur.com/XUF0dsY.jpg)

If we want to turn down the LED, just reverse the procedure:

```bash=
gpio write 24 0
gpio mode 24 in
```
![](https://i.imgur.com/KwP5Hjz.png)
And then you get the initial default setting of GPIO.

We can turn on another LED connect on GPIO 26 (wPi 25) using same method:

```bash=
#change the pinMode to OUTPUT and turn on
gpio mode 25 out
gpio write 25 1

#turn down and change the pinMode to INPUT
gpio write 25 0
gpio mode 25 in
```

*    Note that we need to restore the port to default(INPUT) is important, because in output state might get damaged if connect to GND, therefore we need a current-limiting resistor to avoid bad things happen.

## BlinkLED With C code with WiringPi Package

Source code of WiringPi: [wiringPi.h](https://github.com/WiringPi/WiringPi/blob/master/wiringPi/wiringPi.h) [wiringPi.c](https://github.com/WiringPi/WiringPi/blob/master/wiringPi/wiringPi.c)

### blink.c file makes LED turn on alternativly.
```c=
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
```

Simple Makefile to compile and link the binary file to WiringPi package
```makefile=
CC = gcc
CFLAGS = -g -Wall
LINKER = -lwiringPi

BIN = blink

all: $(BIN)

%: %.c
	$(CC) $(CFLAGS) $< -o $@ $(LINKER)

clean:
	rm -rf $(BIN)
```

```bash=
#compile and run the program:
$ make
$ ./blink
```

Result:
{%youtube 6cgJZMIiKqw%}

If terminate the program with Ctrl C, the command will interupt the code in infinite while loop, therefore, our pinMode still remain OUTPUT mode, and one of LED still on after the program terminated. Of course we can still use bash command to reset all states to default, but it is the response to this little program.

### Adding Interupt Signal into program (blink_improved.c):
```c=
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
```

And update the makefile:
```makefile=
CC = gcc
CFLAGS = -g -Wall
LINKER = -lwiringPi

BIN = blink blink_improved

all: $(BIN)

%: %.c
	$(CC) $(CFLAGS) $< -o $@ $(LINKER)

clean:
	rm -rf $(BIN)
```

Finally, we get three methods to terminate the program with GPIO states reset to default INPUT state. We can check by using gpio readall to monitor all states.
*    1. terminate by ctrl + c
```bash=
$ ./blink_improved
$ ^C
```

*    2. kill by process ID
```bash=
$ ./blink_improved &    #run the program in the background
$ kill [processID]
```

*    3. kill by name
```bash=
$ ./blink_improved &    #run the program in the background
$ pkill blink_improved
```

### Change to GPIO (BCM) number system
Simply change wiringPiSetup() to wiringPiSetupGpio().
```c=
#include <wiringPi.h>
#include <signal.h>

//using default wPi numbering scheme
#define LED1 19
#define LED2 26

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
    wiringPiSetupGpio();    // <- change to Gpio
    
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
```