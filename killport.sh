#!/bin/bash

usage() {
    echo "Usage: $0 -p <port>"
    exit 1
}
if [ "$#" -ne 2 ] || [ "$1" != "-p" ]; then
    usage
fi
port="$2"
pid=$(lsof -t -i :"$port")

if [ -n "$pid" ]; then
    echo "Killing the process using port $port (PID: $pid)..."
    kill -9 "$pid"
    echo "Process killed."
else
    echo "No process found using port $port."
fi
