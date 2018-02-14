#!/bin/bash
trap clean SIGINT 
function clean() {
	pigs i2cc $handle 
	exit 0
}

echo "Lese AMS-IAQ-Sensor"
BUS=1
ADDR="0x5a"
export handle=$(pigs i2co $BUS $ADDR 0)

while true; do
	pigs i2crd $handle 9
	sleep 1
done

