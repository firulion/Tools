#!/bin/bash

while true; do
	TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
	DATA=$(grep -E 'TEMP_CPU|HUMIDITY_LEVEL' event_state.ini)
	echo "[$TIMESTAMP] $DATA" >> log_TH.txt
	sleep 5
done


#ps -ef | grep temp_script.sh
#kill PID