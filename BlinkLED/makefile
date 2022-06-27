CC = gcc
CFLAGS = -g -Wall
LINKER = -lwiringPi

BIN = blink blink_improved blink_bcm_numsystem

all: $(BIN)

%: %.c
	$(CC) $(CFLAGS) $< -o $@ $(LINKER)

clean:
	rm -rf $(BIN)