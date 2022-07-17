CC = gcc
CFLAGS = -g -Wall
LINKER = -lwiringPi -lpthread

BIN = blink blink_improved blink_bcm_numsystem breathingLight

all: $(BIN)

%: %.c
	$(CC) $(CFLAGS) $< -o $@ $(LINKER)

clean:
	rm -rf $(BIN)