#!/bin/sh 

#Daniel Ryaboshapka
#ssh.sh 
#130.64.157.102 master
# 130.64.92.174
SCRIPT="cd mailbox; echo 0 > data.txt"  
#from pybricks import ev3brick as brick; brick.sound.beep();"
sshpass -p "maker" ssh -o StrictHostKeyChecking=no -l robot 130.64.92.174 "$SCRIPT"